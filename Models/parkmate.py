"""
ParkMate AI Assistant
-------------------------------------------------
AI-powered chatbot for bookings, extensions,
and answering parking-related queries.
"""

import random
import logging
import datetime

logging.basicConfig(level=logging.INFO)

class ParkMateAssistant:
    RESPONSES = {
        "book": [
            "Sure! Booking your slot now...",
            "Reservation complete. Enjoy your parking!",
            "Slot confirmed. You will receive a QR shortly."
        ],
        "extend": [
            "Your parking time has been extended successfully.",
            "Done! Extra time added to your booking.",
            "Extension approved. Drive safe!"
        ],
        "help": [
            "I can assist you with booking, extensions, and slot availability.",
            "Need help? Try asking about pricing or availability.",
            "I can also guide you to the nearest available slot."
        ],
        "greet": [
            "Hello! Welcome to ParkMate 🚗",
            "Hi there! Looking for parking assistance?",
            "Good day! Ready to find your perfect spot?"
        ]
    }

    def __init__(self):
        self.chat_history = []
        logging.info("[INIT] ParkMate Assistant activated.")

    def detect_intent(self, message: str) -> str:
        """
        Fake NLP to detect user intent.
        """
        msg = message.lower()
        if "book" in msg:
            return "book"
        elif "extend" in msg:
            return "extend"
        elif "price" in msg:
            return "help"
        elif "hello" in msg or "hi" in msg:
            return "greet"
        return "help"

    def get_response(self, user_message: str) -> str:
        """
        Generate AI-like response.
        """
        intent = self.detect_intent(user_message)
        response = random.choice(self.RESPONSES.get(intent, ["Sorry, I didn’t get that."]))
        self.chat_history.append((datetime.datetime.now(), user_message, response))
        logging.info(f"[CHAT] User='{user_message}', Intent={intent}, Response='{response}'")
        return response

    def show_history(self):
        """
        Show all chat logs.
        """
        return self.chat_history

# Example usage
if __name__ == "__main__":
    assistant = ParkMateAssistant()
    print(assistant.get_response("Hi"))
    print(assistant.get_response("Can you book a slot?"))
    print(assistant.get_response("Extend my booking"))
    print(assistant.show_history())
