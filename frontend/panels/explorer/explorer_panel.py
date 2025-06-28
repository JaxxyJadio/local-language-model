from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget

class ExplorerPanel(QWidget):
    """
    Explorer View (file tree panel)
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(220)

        layout = QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(4)

        # Header
        header = QLabel("EXPLORER")
        header.setStyleSheet("font-weight: bold;")

        # Simple placeholder file list
        self.file_list = QListWidget()
        self.file_list.addItems([
            "main.py",
            "requirements.txt",
            "backend/",
            "frontend/",
            "README.md"
        ])

        layout.addWidget(header)
        layout.addWidget(self.file_list)
        self.setLayout(layout)
