# ---------------------------------------------
# panels/aigent/aigent_chat_window.py
# ---------------------------------------------
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel
from PyQt6.QtCore import Qt

class AIGentChatWindow(QWidget):
    '''
    > panels/aigent/aigent_chat_window.py
    > Represents the main vertical chat history
    > Stretches vertically with the AIGent column
    > Shows conversation with the LLM
    > User and AI messages appear here
    > Scrollable QTextEdit style for reading
    '''
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(2)

        label = QLabel("AIGent Chat Window")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("background-color: #EEE; border: 1px solid black;")

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.chat_area.setPlaceholderText("Conversation will appear here...")
        self.chat_area.setStyleSheet("border: 1px solid black;")

        layout.addWidget(label)
        layout.addWidget(self.chat_area)

        self.setLayout(layout)
