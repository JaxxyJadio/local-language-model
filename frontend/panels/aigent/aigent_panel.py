from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

class AIGentPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(4)

        label = QLabel("🤖 AIgent Panel")
        self.prompt = QTextEdit()
        self.prompt.setPlaceholderText("Type your prompt...")
        self.response = QTextEdit()
        self.response.setReadOnly(True)
        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self.fake_llm_call)

        layout.addWidget(label)
        layout.addWidget(self.prompt)
        layout.addWidget(self.send_btn)
        layout.addWidget(self.response)
        self.setLayout(layout)

    def fake_llm_call(self):
        text = self.prompt.toPlainText()
        self.response.setText(f"AIgent says: {text[::-1]}")
