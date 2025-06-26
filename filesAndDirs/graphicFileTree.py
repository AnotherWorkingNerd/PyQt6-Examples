# This show any graphics files in the currently selected directory
# The user's home directory and its parent directories are 
# expanded when the directory tree is shown.

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QTreeView, 
    QSplitter, QLabel
)
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import Qt, QDir, pyqtSignal
import os

class GraphicsFileBrowser(QWidget):
    fileSelected = pyqtSignal(str)  # Signal to emit fully qualified file name

    def __init__(self, parent=None):
        super().__init__(parent)
        
        print("Initializing GraphicsFileBrowser...")
        self.initUI()

    def initUI(self):
        print("Setting up UI components...")
        layout = QVBoxLayout(self)

        # Create a file system model
        self.model = QFileSystemModel()
        self.model.setRootPath("")  # Allow browsing the entire filesystem
        print("Root path set to the filesystem root.")
        
        # Filter to show only graphics files
        graphics_filters = ["*.png", "*.jpg", "*.jpeg", "*.bmp", "*.gif", "*.tiff"]
        self.model.setNameFilters(graphics_filters)
        self.model.setNameFilterDisables(False)
        print(f"Applied graphics filters: {graphics_filters}")

        # Create a tree view for the directory structure
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        home_index = self.model.index(QDir.homePath())
        self.tree.setRootIndex(self.model.index(QDir.rootPath()))

        # Expand the user's home directory and its parents
        current_index = home_index
        while current_index.isValid():
            self.tree.expand(current_index)
            current_index = current_index.parent()

        self.tree.setSortingEnabled(True)
        self.tree.setAnimated(True)
        self.tree.setIndentation(20)

        # Adjust column widths
        self.tree.header().setSectionResizeMode(0, self.tree.header().ResizeMode.Stretch)
        self.tree.setColumnWidth(0, 300)  # Make the 'Name' column twice as wide

        print("Tree view configured with adjusted column widths and expanded home directory.")

        # Connect the selection event
        self.tree.clicked.connect(self.onFileSelected)
        print("Connected tree view click event to onFileSelected.")

        layout.addWidget(self.tree)
        self.setLayout(layout)

    def onFileSelected(self, index):
        # Get the file path from the selected index
        fqfn = self.model.filePath(index)
        print(f"Item clicked: {fqfn}")
        if os.path.isfile(fqfn):  
            print(f"File selected: {fqfn}")
            self.fileSelected.emit(fqfn)
        else:
            print(f"Not a file: {fqfn}")

# Example usage
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Initializing MainWindow...")
        self.setWindowTitle("Graphics File Browser")
        self.setGeometry(100, 100, 800, 600)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        self.browser = GraphicsFileBrowser()
        # fileSelected signal emittedfrom GraphicsFileBrowser
        self.browser.fileSelected.connect(self.displaySelectedFile)

        self.label = QLabel("Selected file path will appear here.")
        self.label.setWordWrap(True)

        splitter.addWidget(self.browser)
        splitter.addWidget(self.label)

        self.setCentralWidget(splitter)
        print("MainWindow setup complete.")

    def displaySelectedFile(self, fqfn):
        print(f"Displaying selected file: {fqfn}")
        self.label.setText(f"Selected File: {fqfn}")

if __name__ == "__main__":
    print("Starting application...")
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
