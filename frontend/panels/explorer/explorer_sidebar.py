from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class ExplorerSidebar(QWidget):
    """
    Activity Bar (leftmost vertical bar with icons)
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(48)

        layout = QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(4)

        # Add your VS Code-style icons
        buttons = [
            ("📁", "Explorer"),
            ("🔍", "Search"),
            ("🐙", "Source Control"),
            ("🐞", "Debug"),
            ("🧩", "Extensions")
        ]

        for icon, tooltip in buttons:
            btn = QPushButton(icon)
            btn.setToolTip(tooltip)
            btn.setFixedSize(40, 40)
            layout.addWidget(btn)

        layout.addStretch()
        self.setLayout(layout)
