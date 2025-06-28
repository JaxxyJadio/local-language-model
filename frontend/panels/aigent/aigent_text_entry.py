# ---------------------------------------------
# panels/aigent/aigent_text_entry.py
# ---------------------------------------------
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt6.QtCore import Qt

class AIGentTextEntry(QWidget):
    '''
    > panels/aigent/aigent_text_entry.py
    > Fixed 200px high input area for prompts
    > Includes header label and text box
    > Send button at bottom for submitting
    > User types prompts to the LLM here
    > Matches VS Code's sidebar prompt entry UX
    '''
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(4)

        label = QLabel("AIGent Text Entry")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("background-color: #EEE; border: 1px solid black;")

        self.prompt_box = QTextEdit()
        self.prompt_box.setPlaceholderText("Type your prompt here...")
        self.prompt_box.setStyleSheet("border: 1px solid black;")

        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("border: 1px solid black;")

        layout.addWidget(label)
        layout.addWidget(self.prompt_box)
        layout.addWidget(self.send_button)

        self.setLayout(layout)
