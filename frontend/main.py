import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMenuBar, QMenu, QLineEdit, QLabel,
    QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QTabWidget, QSizePolicy
)
from PyQt6.QtCore import Qt

from panels.explorer.explorer_sidebar import ExplorerSidebar
from panels.explorer.explorer_top_panel import ExplorerTopPanel
from panels.explorer.explorer_panel import ExplorerPanel
from panels.explorer.explorer_bottom_panel import ExplorerBottomPanel

from panels.aigent.aigent_sidebar import AIGentSidebar
from panels.aigent.aigent_top_panel import AIGentTopPanel
from panels.aigent.aigent_chat_window import AIGentChatWindow
from panels.aigent.aigent_text_entry import AIGentTextEntry
from panels.aigent.aigent_bottom_panel import AIGentBottomPanel

# ---------------------------------------------
# MAIN
# ---------------------------------------------
class Main(QMainWindow):
    '''
    > panels/main.py
    > The entire VS Code-like layout in one single class
    > Explorer Column, EditorPanel with tabs, AIGent Column
    > Top/Bottom fixed 200px with outlines
    > Sidebar on far left and right
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VS Code Clone - PyQt6 Edition")
        self.resize(1600, 900)

        central = QWidget()
        main_vbox = QVBoxLayout()
        main_vbox.setContentsMargins(0, 0, 0, 0)
        main_vbox.setSpacing(0)

        # ---------------------------------------------
        # Menu Bar with Search Field
        # ---------------------------------------------
        menubar = QMenuBar()
        for name in ["File", "Edit", "Selection", "LAN", "LLM", "JdoNet", "Code Doctor", "Plugins", "Settings", "Help"]:
            menubar.addMenu(QMenu(name))
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search")
        menubar.setCornerWidget(search_bar, Qt.Corner.TopRightCorner)
        self.setMenuBar(menubar)

        # ---------------------------------------------
        # Center Row with all Columns
        # ---------------------------------------------
        center_row = QHBoxLayout()
        center_row.setContentsMargins(0, 0, 0, 0)
        center_row.setSpacing(0)

        # Explorer Sidebar
        center_row.addWidget(ExplorerSidebar())

        # ---------------------------------------------
        # Explorer Column (Top / Panel / Bottom)
        # ---------------------------------------------
        explorer_column = QVBoxLayout()
        explorer_column.setContentsMargins(0, 0, 0, 0)
        explorer_column.setSpacing(0)

        explorer_top = ExplorerTopPanel()
        explorer_top.setFixedHeight(200)
        explorer_top.setStyleSheet("border: 1px solid black;")
        explorer_column.addWidget(explorer_top)

        explorer_mid = ExplorerPanel()
        explorer_mid.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        explorer_column.addWidget(explorer_mid)

        explorer_bottom = ExplorerBottomPanel()
        explorer_bottom.setFixedHeight(200)
        explorer_bottom.setStyleSheet("border: 1px solid black;")
        explorer_column.addWidget(explorer_bottom)

        explorer_container = QWidget()
        explorer_container.setLayout(explorer_column)
        explorer_container.setFixedWidth(220)
        center_row.addWidget(explorer_container)

        # ---------------------------------------------
        # EditorPanel (single unified tabs)
        # ---------------------------------------------
        editor_panel = QTabWidget()
        editor_panel.setTabPosition(QTabWidget.TabPosition.North)
        editor_panel.setMovable(True)
        editor_panel.setStyleSheet("border: 1px solid black;")
        editor_panel.addTab(self.makeEditor("// Welcome to your VS Code Clone"), "welcome.md")
        editor_panel.addTab(self.makeEditor("# main.py\nprint('Hello')"), "main.py")
        editor_panel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        center_row.addWidget(editor_panel, 4)

        # ---------------------------------------------
        # AIGent Column (Top / Chat / Entry / Bottom)
        # ---------------------------------------------
        aigent_column = QVBoxLayout()
        aigent_column.setContentsMargins(0, 0, 0, 0)
        aigent_column.setSpacing(0)

        aigent_top = AIGentTopPanel()
        aigent_top.setFixedHeight(200)
        aigent_top.setStyleSheet("border: 1px solid black;")
        aigent_column.addWidget(aigent_top)

        aigent_chat = AIGentChatWindow()
        aigent_chat.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        aigent_column.addWidget(aigent_chat)

        aigent_entry = AIGentTextEntry()
        aigent_entry.setFixedHeight(200)
        aigent_entry.setStyleSheet("border: 1px solid black;")
        aigent_column.addWidget(aigent_entry)

        aigent_bottom = AIGentBottomPanel()
        aigent_bottom.setFixedHeight(200)
        aigent_bottom.setStyleSheet("border: 1px solid black;")
        aigent_column.addWidget(aigent_bottom)

        aigent_container = QWidget()
        aigent_container.setLayout(aigent_column)
        aigent_container.setFixedWidth(300)
        center_row.addWidget(aigent_container)

        # AIGent Sidebar
        center_row.addWidget(AIGentSidebar())

        # Add Center Row
        center_widget = QWidget()
        center_widget.setLayout(center_row)
        main_vbox.addWidget(center_widget)

        # ---------------------------------------------
        # Done
        # ---------------------------------------------
        central.setLayout(main_vbox)
        self.setCentralWidget(central)

    def makeEditor(self, content):
        '''
        > panels/main.py
        > Helper to create a QTextEdit for a tab
        > Fills it with starter content
        > Sets Expanding policy so it grows
        > Used in EditorPanel tabs above
        '''
        editor = QTextEdit()
        editor.setText(content)
        editor.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        return editor

# ---------------------------------------------
# APP ENTRY
# ---------------------------------------------
if __name__ == "__main__":
    '''
    > panels/main.py
    > The standard PyQt6 entry point
    > Creates QApplication, opens Main window
    > Enters main event loop
    > Allows user interaction
    '''
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())
