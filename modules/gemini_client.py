import google.generativeai as genai
import json
import os
import logging
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

CONFIG_PATH = os.path.join('config', 'config.json')
HISTORY_PATH = os.path.join('config', 'chat_history.json')

def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

class GeminiClient:
    """
    GeminiClient class for handling the Gemini API with features like chat history and tune management.
    """

    def __init__(self, history_file: str = HISTORY_PATH):
        genai.configure(api_key=GEMINI_API_KEY)
        self.history_file = history_file

        self.config = load_config()
        self.tune = self.config.get('tune')
        if not self.tune:
            self.tune = self.config.get('default_tune')
        self.model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=self.tune)
        self.chat = self.model.start_chat()
        self.load_chat_history()
        logging.info(f"GeminiClient initialized with tune: {self.tune}")

    def change_tune(self, tune: str):
        if not tune:
            tune = self.config.get('default_tune')
        self.tune = tune
        self.config['tune'] = tune
        save_config(self.config)
        self.model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=self.tune)
        self.chat = self.model.start_chat()
        logging.info(f"Tune changed to: {self.tune}")

    def generate_response(self, message: str, author: str) -> str:
        try:
            response = self.chat.send_message(message)
            logging.info(f"Generated response for message from {author} : {message}")
        except Exception as e:
            logging.error("Error in generating response", exc_info=True)
            return "System error."
        self.save_chat_history()
        return response.text

    def clear_tune(self):
        self.change_tune(self.config['default_tune'])
        self.clear_chat_history()
        logging.info("Tune cleared")

    def save_tune(self):
        self.config['tune'] = self.tune
        save_config(self.config)
        logging.info("Tune saved to config.json")

    def load_tune(self):
        self.config = load_config()
        self.tune = self.config.get('tune')
        if not self.tune:
            self.tune = self.config.get('default_tune')

    def set_history_file(self, history_file: str):
        self.history_file = history_file
        if os.path.exists(self.history_file):
            self.load_chat_history()
        else:
            self.save_chat_history()
        logging.info(f"History file set to: {history_file}")

    def clear_chat_history(self):
        self.chat = self.model.start_chat()
        self.save_chat_history()
        logging.info("Chat history cleared")

    def save_chat_history(self):
        chat_history_serializable = [
            {
                "parts": [{"text": part.text} for part in entry.parts],
                "role": entry.role
            }
            for entry in self.chat.history
        ]
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(chat_history_serializable, f, ensure_ascii=False, indent=4)
        with open(self.history_file + '.backup', 'w', encoding='utf-8') as f:
            json.dump(chat_history_serializable, f, ensure_ascii=False, indent=4)
        logging.info(f"Chat history saved to file: {self.history_file}")

    def load_chat_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r', encoding='utf-8') as f:
                chat_history_serializable = json.load(f)
                self.chat_history = chat_history_serializable
                self.chat = self.model.start_chat(history=[
                    {
                        "parts": [{"text": part["text"]} for part in entry["parts"]],
                        "role": entry["role"]
                    }
                    for entry in chat_history_serializable
                ])
            logging.info("Chat history loaded from file")
        else:
            self.chat = self.model.start_chat()
            logging.info("No chat history file found, starting new chat")

    def shutdown(self):
        self.save_chat_history()
        self.save_tune()
        logging.info("Shutting down GeminiClient")
        return True