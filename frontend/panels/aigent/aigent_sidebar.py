from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class AIGentSidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(48)
        layout = QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(4)

        # Example sidebar buttons
        for icon in ["🤖", "📜", "⚙️"]:
            btn = QPushButton(icon)
            btn.setFixedSize(40, 40)
            layout.addWidget(btn)

        layout.addStretch()
        self.setLayout(layout)
