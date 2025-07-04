# how to create a “Context Menu” and sub-context Menu
# see: https://youtu.be/99zfeWcxy0I
# and: https://coderslegacy.com/python/pyqt6-context-menu/ but it doesn't contain the sub menu stuff.

from PyQt6.QtWidgets import QWidget, QMenu, QApplication
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create the context menu and add some actions
        self.context_menu = QMenu(self)
        action1 = self.context_menu.addAction("Action 1")
        action2 = self.context_menu.addAction("Action 2")
        action3 = self.context_menu.addAction("Action 3")

        # Connect the actions to methods
        action1.triggered.connect(self.action1_triggered)
        action2.triggered.connect(self.action2_triggered)
        action3.triggered.connect(self.action3_triggered)
        self.show()

 		# create sub-context menus
        self.file_menu = QMenu(self, title = "File")
        f_action1 = self.file_menu.addAction("Open")
        f_action2 = self.file_menu.addAction("Save")
        f_action3 = self.file_menu.addAction("Delete")

        # connect f_action[1-3] the same way as the other Actions are connected.

        self.context_menu.addMenu(self.file_menu)

        self.show()

    def contextMenuEvent(self, event):
        # Show the context menu
        self.context_menu.exec(event.globalPos())

    def action1_triggered(self):
        # Handle the "Action 1" action
        pass

    def action2_triggered(self):
        # Handle the "Action 2" action
        pass

    def action3_triggered(self):
        # Handle the "Action 3" action
        pass


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec())
