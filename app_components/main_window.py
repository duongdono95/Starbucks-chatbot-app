import json
import pickle
import random
from PySide6 import QtWidgets
from .SideBar.sidebar import MenuBar
from .ConversationArea.conversation_area import ConversationArea
import uuid
import datetime
from functions import clean_text

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Starbuck Chatbot")
        
        with open("models/nlp.pkl", "rb") as f:
            self.nlp = pickle.load(f)
        with open("models/vectorizer.pkl", "rb") as f:
            self.vectorise_model = pickle.load(f)
        with open("models/model.pkl", "rb") as f:
            self.model = pickle.load(f)
        with open("datasets/label_mapping.json", "r") as f:
            self.label_mapping = json.load(f)
        with open("datasets/dataset.json", "r") as f:
            self.dataset = json.load(f)
        
        self.conversation = {
            "id": str(uuid.uuid4()),
            "messages": []
        }

        self.current_message = ""
        
        container = QtWidgets.QWidget()
        self.setCentralWidget(container)
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(5, 5, 5, 5)

        layout.setSpacing(10)

        self.menu_bar = MenuBar(self)
        self.conversation_box = ConversationArea(self)

        layout.addWidget(self.menu_bar, 1)
        layout.addWidget(self.conversation_box, 3)
       
    def send_message(self, is_human):
        if self.current_message.strip(): 
            message_id = str(uuid.uuid4()) 
            timestamp = datetime.datetime.now().isoformat() + "Z" 
            new_message = {
                "id": message_id,
                "role": "human",
                "content": self.current_message.strip(), 
                "intent": "", 
                "timestamp": timestamp
            }

            self.conversation["messages"].append(new_message)
            
            self.conversation_box.output_area.update_messages()
            self.conversation_box.input_area.user_input.clear()
            self.current_message = "" 
            
            print("Main - ", self.conversation["messages"])
        else:
            print("No message available")
    
    def produce_answer(self, text):
        cleaned_text = clean_text(text, self.nlp)
        vectorised_text = self.vectorise_model.transform([cleaned_text])
        result = self.model.predict(vectorised_text.toarray())
        for item in self.dataset:
            if item["intent"] == self.label_mapping[str(result[0])]:
                answer =  random.choice(item["responses"])
                break
            else:
                answer = "Sorry, I don't understand."
        self.send_message()
            