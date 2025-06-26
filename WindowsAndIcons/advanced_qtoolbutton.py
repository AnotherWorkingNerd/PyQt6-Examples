# SRC: https://coderscratchpad.com/pyqt6-using-qtoolbutton-for-toolbars/
#
# PyQt6 QToolbar functionality 

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolButton, QToolBar, QMessageBox
from PyQt6.QtGui import QIcon

# Slot function to handle button click
def on_tool_button_toggled(checked):
    QMessageBox.information(window, 'Button Toggled', f'Tool Button is {"checked" if checked else "unchecked"}!')

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create a QMainWindow instance (main window)
window = QMainWindow()
window.setWindowTitle('Advanced QToolButton Features')
window.setGeometry(100, 100, 600, 400)

# Create a QToolBar instance
toolbar = QToolBar(window)
window.addToolBar(toolbar)

# Create a QToolButton instance
tool_button = QToolButton()
tool_button.setText('Tool Button')
tool_button.setIcon(QIcon('path/to/icon.png'))  # Set an icon for the button
tool_button.setCheckable(True)  # Make the button checkable
tool_button.setAutoRaise(True)  # Enable auto-raise feature

# Connect the button toggled signal to the slot function
tool_button.toggled.connect(on_tool_button_toggled)

# Add the QToolButton to the toolbar
toolbar.addWidget(tool_button)

# Show the main window
window.show()

# Run the application's event loop
sys.exit(app.exec())