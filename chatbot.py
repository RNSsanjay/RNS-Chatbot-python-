import customtkinter as ctk
from datetime import datetime
import re


class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.user_data = {}

        # Configure dark theme appearance
        ctk.set_appearance_mode("Dark")  # Options: "System", "Dark", "Light"
        ctk.set_default_color_theme("dark-blue")  # Options: "blue", "dark-blue", "green"

        # Configure main window
        self.root.title("RNS Chatbot 🤖")
        self.root.geometry("800x800")
        self.root.resizable(False, False)

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.header = ctk.CTkLabel(
            self.root,
            text="RNS Chatbot 🤖",
            font=("Arial", 22, "bold"),
            text_color="#E5E5E5",
            corner_radius=10,
        )
        self.header.grid(row=0, column=0, columnspan=2, pady=(10, 0), padx=10, sticky="ew")

        # Chat display area
        self.chat_frame = ctk.CTkScrollableFrame(self.root, width=720, height=650, corner_radius=10)
        self.chat_frame.grid(row=1, column=0, columnspan=2, padx=15, pady=10)

        # User input field
        self.user_input = ctk.CTkEntry(
            self.root,
            placeholder_text="Type your message here...",
            font=("Arial", 14),
            width=600,
            height=40,
            border_width=2,
            corner_radius=5,
        )
        self.user_input.grid(row=2, column=0, padx=(15, 5), pady=10, sticky="w")
        self.user_input.bind("<Return>", self.send_message)

        # Send button
        self.send_button = ctk.CTkButton(
            self.root,
            text="Send",
            command=self.send_message,
            font=("Arial", 14, "bold"),
            width=120,
            height=40,
            corner_radius=5,
        )
        self.send_button.grid(row=2, column=1, padx=(5, 15), pady=10, sticky="e")

    def send_message(self, event=None):
        user_message = self.user_input.get().strip()
        if user_message:
            self.display_message(f"You: {user_message}", sender="user")
            self.user_input.delete(0, ctk.END)
            self.respond_to_message(user_message)

    def display_message(self, message, sender="bot"):
        text_color = "#FFFFFF" if sender == "user" else "#A5A5A5"
        bubble_bg = "#1E1E1E" if sender == "bot" else "#333333"

        message_frame = ctk.CTkFrame(self.chat_frame, fg_color=bubble_bg, corner_radius=10)
        message_frame.pack(fill="x", pady=5, padx=10, anchor="e" if sender == "user" else "w")

        message_label = ctk.CTkLabel(
            message_frame,
            text=message,
            font=("Arial", 14),
            justify="left",
            text_color=text_color,
            anchor="w",
            padx=10,
            pady=5,
        )
        message_label.pack(fill="x")

    def respond_to_message(self, message):
        response = self.get_response(message)
        self.display_message(f"Chatbot: {response}", sender="bot")

    def get_response(self, message):
        # Dynamic response system
        message = message.lower()

        # Recognize and store user details
        name_match = re.search(r"my name is (\w+)", message)
        age_match = re.search(r"my age is (\d+)", message)
        color_match = re.search(r"my favorite color is (\w+)", message)

        if name_match:
            name = name_match.group(1)
            self.user_data["name"] = name
            return f"Got it! I'll remember that your name is {name}."

        if age_match:
            age = age_match.group(1)
            self.user_data["age"] = age
            return f"Great! I'll remember that you're {age} years old."

        if color_match:
            color = color_match.group(1)
            self.user_data["favorite_color"] = color
            return f"Awesome! Your favorite color is {color}."

        if "what is my name" in message:
            return f"Your name is {self.user_data.get('name', 'not set yet.')}"

        if "what is my age" in message:
            return f"Your age is {self.user_data.get('age', 'not set yet.')}"

        if "what is my favorite color" in message:
            return f"Your favorite color is {self.user_data.get('favorite_color', 'not set yet.')}"

        # General questions
        if "what time is it" in message:
            return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

        if "tell me a joke" in message:
            return "Why don't scientists trust atoms? Because they make up everything!"

        if "how are you" in message:
            return "I'm here and ready to help! How can I assist you today?"

        if "bye" in message:
            return "Goodbye! Have a fantastic day!"

        if "hii" in message:
            return "Welcome you to RNS Chatbot"

        if "hello" in message:
             return "Welcome you to RNS Chatbot"

        return "I'm not sure about that. Could you try rephrasing?"

if __name__ == "__main__":
    app_root = ctk.CTk()
    app = ChatbotApp(app_root)
    app_root.mainloop()
