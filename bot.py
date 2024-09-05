import flet as ft
import spacy
from datetime import datetime

# Load the small English language model
nlp = spacy.load("en_core_web_sm")

# Pre-defined responses
responses = {
    'greet': 'Hello! How can I assist you today?',
    'farewell': 'Goodbye! Have a great day!',
    'how_are_you': 'I am a bot, so I do not have feelings, but thank you for asking!',
    'ask_time': f'The current time is {datetime.now().strftime("%H:%M:%S")}.',
    'ask_name': 'I am just a humble chatbot with no name, but you can call me Bot!',
    'ask_weather': 'I am not connected to a weather service, but it\'s always sunny in the digital world!',
    'thank_you': 'You are welcome!',
    'default': 'I am not sure how to respond to that. Could you rephrase?'
}

# Function to determine intent
def determine_intent(doc):
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return 'greet'
        elif token.lemma_ in ["bye", "goodbye", "see you"]:
            return 'farewell'
        elif "how" in token.text.lower() and "you" in token.text.lower():
            return 'how_are_you'
        elif token.lemma_ in ["time", "clock"]:
            return 'ask_time'
        elif token.lemma_ in ["name", "who"]:
            return 'ask_name'
        elif token.lemma_ in ["weather", "rain", "sun"]:
            return 'ask_weather'
        elif token.lemma_ in ["thank", "thanks"]:
            return 'thank_you'
    return 'default'

# Function to get response based on user input
def get_response(user_input):
    doc = nlp(user_input)
    intent = determine_intent(doc)
    return responses[intent]

# Flet App
def main(page: ft.Page):
    # Define the AppBar
    app_bar = ft.AppBar(
        title=ft.Text("Chat"),
        leading=ft.Icon(ft.icons.ARROW_BACK),
        bgcolor=ft.colors.BLUE_GREY_900,
    )
    
    # Message List
    messages = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=True,
    )
    
    # Input field and Send button
    input_field = ft.TextField(
        hint_text="Type a message",
        expand=True,
        border_radius=20,
    )
    
    def send_message(e):
        user_message = input_field.value
        if user_message.strip():
            # Display user message as a bubble
            user_bubble = ft.Container(
                content=ft.Text(user_message, color=ft.colors.WHITE),
                padding=ft.padding.all(10),
                bgcolor=ft.colors.BLUE_GREY_700,
                border_radius=ft.border_radius.all(20),
                # No width specified, so it will be based on content
            )
            
            # Align the user message bubble to the right
            messages.controls.append(
                ft.Row(
                    controls=[user_bubble],
                    alignment=ft.MainAxisAlignment.END,
                )
            )
            
            # Get bot response
            bot_response = get_response(user_message)
            
            # Display bot message as a bubble
            bot_bubble = ft.Container(
                content=ft.Text(bot_response, color=ft.colors.WHITE),
                padding=ft.padding.all(10),
                bgcolor=ft.colors.BLUE_GREY_900,
                border_radius=ft.border_radius.all(20),
                # No width specified, so it will be based on content
            )
            
            # Align the bot message bubble to the left
            messages.controls.append(
                ft.Row(
                    controls=[bot_bubble],
                    alignment=ft.MainAxisAlignment.START,
                )
            )
            
            # Clear the input field
            input_field.value = ""
            page.update()
    
    send_button = ft.IconButton(
        icon=ft.icons.SEND,
        on_click=send_message,
        icon_color=ft.colors.BLUE_GREY_900,
    )
    
    # Bottom input row
    input_row = ft.Row(
        controls=[input_field, send_button],
        spacing=10,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    
    # Main layout
    page.add(
        app_bar,
        messages,
        input_row,
    )

# Run the Flet app
ft.app(target=main)
