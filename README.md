# 📱 Interactive Chatbot UI with Flet and spaCy 🤖
This repository contains a chatbot interface built with Flet for the UI and spaCy for Natural Language Processing (NLP). The app provides a fully responsive chat interface, where the user can input text, and the chatbot responds based on intent analysis.

🛠️ Features
Interactive chat interface 🎨
Bot responses based on intent recognition using spaCy 🧠
Responsive design 📱
Predefined responses for common conversational intents 💬
🔧 Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/chatbot-ui-flet-spacy.git
cd chatbot-ui-flet-spacy
2. Install Dependencies
Ensure you have Python installed, and then install the required libraries:

bash
Copy code
pip install flet spacy
python -m spacy download en_core_web_sm
3. Run the application
bash
Copy code
python main.py
🚀 Usage
After running the app, you'll see a simple chat interface where you can type messages, and the bot will respond. The bot recognizes intents like greetings, farewells, and requests for time and name, among others.

📜 Code Explanation
The project consists of several key components. Let’s walk through the code step by step:

1. Importing Libraries
python
Copy code
import flet as ft
import spacy
from datetime import datetime
We import flet for building the UI, spacy for Natural Language Processing, and datetime to provide the current time if requested by the user.

2. Loading the spaCy Language Model
python
Copy code
nlp = spacy.load("en_core_web_sm")
This loads the small English language model for spaCy, which helps in identifying intents from user input.

3. Predefined Responses
python
Copy code
responses = {
    'greet': 'Hello! How can I assist you today?',
    'farewell': 'Goodbye! Have a great day!',
    ...
}
This dictionary holds the chatbot's predefined responses for different user intents like greetings, farewells, and asking for the current time.

4. Intent Recognition Function
python
Copy code
def determine_intent(doc):
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return 'greet'
        ...
This function processes the user input and determines which predefined response to use by analyzing the tokens (words) in the message.

5. Getting Response Based on User Input
python
Copy code
def get_response(user_input):
    doc = nlp(user_input)
    intent = determine_intent(doc)
    return responses[intent]
This function takes the user input, runs it through the intent recognition function, and returns the appropriate response from the responses dictionary.

6. Building the Chat Interface with Flet
python
Copy code
def main(page: ft.Page):
The main() function is the core of the Flet application, which builds the UI.

6.1 AppBar
python
Copy code
app_bar = ft.AppBar(
    title=ft.Text("Chat"),
    leading=ft.Icon(ft.icons.ARROW_BACK),
    bgcolor=ft.colors.BLUE_GREY_900,
)
The AppBar creates a header with a title and a back arrow, similar to a mobile chat app.

6.2 Message List
python
Copy code
messages = ft.ListView(
    expand=True,
    spacing=10,
    padding=10,
    auto_scroll=True,
)
This is where the user messages and bot responses will be displayed. The ListView is scrollable and auto-adjusts when new messages are added.

6.3 Input Field and Send Button
python
Copy code
input_field = ft.TextField(
    hint_text="Type a message",
    expand=True,
    border_radius=20,
)
send_button = ft.IconButton(
    icon=ft.icons.SEND,
    on_click=send_message,
    icon_color=ft.colors.BLUE_GREY_900,
)
The input field allows the user to type messages, and the send button triggers the send_message() function.

7. Handling User Messages
python
Copy code
def send_message(e):
    user_message = input_field.value
    ...
This function handles the event when the user clicks the "send" button. It processes the user message, generates a chatbot response, and updates the UI with both.

7.1 Displaying User Messages
python
Copy code
user_bubble = ft.Container(
    content=ft.Text(user_message, color=ft.colors.WHITE),
    padding=ft.padding.all(10),
    bgcolor=ft.colors.BLUE_GREY_700,
    border_radius=ft.border_radius.all(20),
)
The user message is wrapped in a Container styled as a chat bubble with padding and a background color.

7.2 Displaying Bot Responses
python
Copy code
bot_response = get_response(user_message)
bot_bubble = ft.Container(
    content=ft.Text(bot_response, color=ft.colors.WHITE),
    padding=ft.padding.all(10),
    bgcolor=ft.colors.BLUE_GREY_900,
    border_radius=ft.border_radius.all(20),
)
The bot's response is also displayed in a styled bubble but aligned on the left, opposite the user's bubble.

8. Final Layout
python
Copy code
page.add(app_bar, messages, input_row)
This finalizes the UI layout by adding the AppBar, message list, and the input row at the bottom of the screen.

🌟 Future Enhancements
Add support for more dynamic intent recognition.
Allow the chatbot to fetch real-time data like weather or time from APIs.
Improve UI with more advanced animations and themes.
👨‍💻 Contributing
Feel free to submit pull requests or open issues to suggest new features or report bugs. Contributions are always welcome!

📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.
