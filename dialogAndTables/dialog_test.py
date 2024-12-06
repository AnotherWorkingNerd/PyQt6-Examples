# 

import sys
from PyQt6.QtCore import Qt, QSize, QDir
from PyQt6.QtGui import QAction, QPixmap, QIcon, QFont
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QScrollArea,
    QToolBar, QDialog, QTableWidget, QTableWidgetItem, QPushButton,
    QCheckBox, QWidget, QFileDialog, QDialogButtonBox
)

class ExampleDialog(QDialog):
    '''
    OK this is mass overkill for a dialog box 
    but I wanted to see just what could be done with a
    Dialog to display metadata in a stylzed table.
    '''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Table Example')
        self.setGeometry(200, 200, 600, 400)
        
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        dlg_btn = (QDialogButtonBox.StandardButton.Ok)
#         dlg_btn = (QDialogButtonBox.StandardButton.Close)
        self.ok_btn = QDialogButtonBox(dlg_btn)
        self.ok_btn.accepted.connect(self.accept)

        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Country', 'Capital'])

        fontsize = 15
        fontname = 'Arial'
        self.table.setFont(QFont(fontname, fontsize))
        self.populate_table(self.table)
        

        self.table.setColumnWidth(0, 15)
        self.table.setColumnWidth(1, 15)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.setWordWrap(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.table)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)
        
    def populate_table(self, table):
        """Populate the table with data from a dict."""

        # Something fairly Generic capitals of countreies.
        capitals = {
            "Albania": "Tirana",
            "Switzerland": "Bern",
            "Latvia": "Riga",
            "Austria": "Vienna",
            "Estonia": "Tallinn",
            "Belgium": "Brussels",
            "Montenegro": "Podgorica",
            "Croatia": "Zagreb",
            "Cyprus": "Nicosia",
            "Germany": "Berlin",
            "Denmark": "Copenhagen",
            "Monaco": "Monaco",
            "Finland": "Helsinki",
            "France": "Paris",
            "Georgia": "Tbilisi", 
            "Slovenia": "Ljubljana", 
        }

        self.table.setRowCount(len(capitals.keys()))

        for row, (key, value) in enumerate(capitals.items()):
            self.table.setItem(row, 0, QTableWidgetItem(str(key)))
            self.table.setItem(row, 1, QTableWidgetItem(str(value)))

    def set_table_style(self):
        """Apply custom colors and styles to the table. Ignored for now."""

        # I like these fonts:
        # https://coolors.co/font/baumans
        # https://coolors.co/font/convergence
        # lots of interesting stuff at: https://coolors.co/fonts

        # fontsize = 16
        # fontname = 'Arial'
        # self.table.setFont(QFont(fontname, fontsize))
        pass

        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #2e3440;   /* Table background color */
                color: #d8dee9;                 /* Text color */
                gridline-color: #3b4252;     /* Grid lines color */
            }
            QHeaderView::section {
                background-color: #4c566a;   /* Header background */
                color: #eceff4;                 /* Header text color */
                font-weight: bold;
            }
            QTableWidget::item:selected {
                background-color: #5e81ac;   /* Selected cell background */
                color: #eceff4;                 /* Selected text color */
            }
        """)

    def button_clicked(self, btn):
        role = buttonBox.standardButton(btn)
        if role == QDialogButtonBox.Ok:
#            if role == QDialogButtonBox.Close:
            print('clicked ok')
            # close dialog box

class MainWindow(QMainWindow):
    '''
    Main application window with a button to open the secondary window.
    '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 600, 300)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # add QLabel
        self.label_text = QLabel()
        self.label_text.setFont(QFont('Georgia', 20))
        self.label_text.setText('Hello.')

        self.layout.addWidget(self.label_text)

        # Menu bar
        self.init_menu_bar()

        # Toolbar
        self.init_tool_bar()

    def init_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        quit_action = QAction('Quit', self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

    def init_tool_bar(self):
        QDir.addSearchPath('icon', './icons/')
        # usage: icon = QtGui.QIcon('icon:myicon.png')

        # Stylesheet code to change the icon based on state.
        # I've seen both !checked and unchecked 
        # I don't think I need 
        #     QCheckBox::indicator {
        #         width: 20px;
        #         height: 20px;
        #     }  
        checkbox_style = """
            QCheckBox::indicator:unchecked {
                image: url('./icons/Checkov.svg');
            }
            QCheckBox::indicator:!checked {
                image: url('./icons/Checkov.svg');
            }
            QCheckBox::indicator:checked {
                image: url('./icons/CheckOn.svg');
            }
            """
            # Any Trek fans out there? LOL

        toolbar = QToolBar('Tools', self)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)
        # toolbar.setIconSize(QSize(32, 32))  # Adjust icon size as needed 
        # toolbar.setIconSize(QSize(64, 64))  # Adjust icon size as needed 
        toolbar.setIconSize(QSize(56, 56))  # Adjust icon size as needed 
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        
        # Its a cheesy generic name... tbb = Tool Bar Button 
        # Add 4 example buttons
        tbb1 = QAction(QIcon('icon:clock-icon.svg'), 'Show table', self)
        tbb1.triggered.connect(self.open_dialog)

        tbb2 = QAction(QIcon('icon:stapler-icon.svg'), 'Stapler', self)
        _tbb2_joke = "What did the staple say to the paper? I’m feeling a bit attached to you."
        tbb2.triggered.connect(lambda: self.update_label(_tbb2_joke))

        tbb3 = QAction(QIcon('icon:pen-icon.svg'), 'Pen and ink', self)
        _tbb3_joke = 'I bought a pen that can write underwater...  it can write other words as well.'
        tbb3.triggered.connect(lambda: self.update_label(_tbb3_joke))

        tbb4 = QAction(QIcon('icon:compass-ruler-icon.svg'), 'Compass', self)
        _tbb4_joke = "What's the point? We're just going round in circles."
        tbb4.triggered.connect(lambda: self.update_label(_tbb4_joke))

        toolbar.addSeparator()
        check_btn = QAction(QIcon("icon:telephone-icon.svg"), "Telephone", self)
        check_btn.setShortcut('Ctrl+T')
        check_btn.setCheckable(True)
        _de_joke = 'Why does Mr Potato Head have a phone.? In case Mr Onion Rings.'
        check_btn.triggered.connect(lambda: self.update_label(_de_joke))
        # do I really need a status tip... 
        check_btn.setStatusTip("its a bit dingy")
        # I believe I can add the clicked and not clicked states using QSS.
        # obj.setStyleSheet("QCheckBox:checked { image: url(dropdown.png) }")
        #  QCheckBox:checked { color: white } 
        # And maybe even  QCheckBox:checked { image: dropdown.png }
        # or { image: url(dropdown.png) }
        # I think the not checked version is  QCheckBox:!checked { color: white }
        
        toolbar.addSeparator()
        self.check_bx = QAction(QIcon("icon:CheckOn.svg"), "another checkbox", self)
        # self.check_btn.setShortcut('Ctrl+T')
        self.check_bx.setCheckable(True)
        # _de_joke = 'Why does Mr Potato Head have a phone.? In case Mr Onion Rings.'
        self.check_bx.triggered.connect(self.checkbox_state)
        # do I really need a status tip... 
        self.check_bx.setStatusTip("Any Wodka?")
        toolbar.addSeparator()
             
        toolbar.addAction(tbb1)
        toolbar.addAction(tbb2)
        toolbar.addAction(tbb3)
        toolbar.addAction(tbb4)
        toolbar.addAction(check_btn)
        toolbar.addAction(self.check_bx)

    def open_dialog(self):
        dialog = ExampleDialog(self)
        dialog.exec()

    def update_label(self, bad_joke):
        # self.label_text.setText('')
        self.label_text.setText(bad_joke)
        self.label_text.adjustSize()
        self.layout.update()
        # update a QLabel with string passed in
    
    def checkbox_state(self):
        activated = self.check_bx.isChecked()
        if activated:
            self.check_bx.setIcon(QIcon('icon:checkov.svg'))
            self.layout.update()
        if not activated:
            self.check_bx.setIcon(QIcon('icon:checkOn.svg'))
            self.layout.update()
            # self.normalSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
