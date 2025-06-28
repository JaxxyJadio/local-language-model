from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class AIGentTopPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(60)
        layout = QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(2)

        label = QLabel("aigent top panel")
        layout.addWidget(label)

        self.setLayout(layout)
