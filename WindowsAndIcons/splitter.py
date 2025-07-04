
# THIS WILL NEED WORK.
# need to replace the following with something simple.
#       FileTreeView()   - what is say a simple file tree.
#       ThumbnailView() - maybe just a grid of labels or something. how blocks that the original TN_viewer used
#       MetadataView()  - maybe create a basic table or something


import sys
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QSplitter, QToolBar, QApplication
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Collapsible Sections Example')
        self.setGeometry(100, 100, 1200, 800)

        # Main layout and splitter
        main_layout = QVBoxLayout()
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.filetree_view = FileTreeView()
        self.thumbnail_view = ThumbnailView()
        self.metadata_view = MetadataView()

        self.splitter.addWidget(self.filetree_view)
        self.splitter.addWidget(self.thumbnail_view)
        self.splitter.addWidget(self.metadata_view)

        self.splitter.setSizes([300, 600, 300])
        self.filetree_view.setMinimumWidth(150)
        self.thumbnail_view.setMinimumWidth(300)
        self.metadata_view.setMinimumWidth(150)

        main_layout.addWidget(self.splitter)

        # Set up toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        # Set icon size for toolbar buttons
        toolbar.setIconSize(QSize(24, 24))  # Adjust icon size as needed

        # Toggle left panel action
        toggle_left_action = QAction(QIcon("path/to/left_icon.png"), "Toggle Left Panel", self)
        toggle_left_action.triggered.connect(self.toggle_left_panel)
        toolbar.addAction(toggle_left_action)

        # Toggle right panel action
        toggle_right_action = QAction(QIcon("path/to/right_icon.png"), "Toggle Right Panel", self)
        toggle_right_action.triggered.connect(self.toggle_right_panel)
        toolbar.addAction(toggle_right_action)

        # Display text labels with icons
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

    def toggle_left_panel(self):
        sizes = self.splitter.sizes()
        if sizes[0] > 0:
            self.splitter.setSizes([0, sizes[1] + sizes[0], sizes[2]])  # Collapse left
        else:
            self.splitter.setSizes([300, sizes[1] - 300, sizes[2]])     # Restore left size

    def toggle_right_panel(self):
        sizes = self.splitter.sizes()
        if sizes[2] > 0:
            self.splitter.setSizes([sizes[0], sizes[1] + sizes[2], 0])  # Collapse right
        else:
            self.splitter.setSizes([sizes[0], sizes[1] - 300, 300])     # Restore right size

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
