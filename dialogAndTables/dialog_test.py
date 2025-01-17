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

        # Define fonts and colors
        fontsize = 15
        fontname = 'Arial'
        background_color = "#5A5A5A"    # light blue
        alternate_color = "#00246B"     # dark blue
        header_color = "#0B2E40"        # dark indigo
        text_color = "#FFFFFF"          # White

        # other good combos
        # "{ alternate-background-color: white; background-color: gray; }"      # white text unless otherwise noted
        # "{ alternate-background-color: white; background-color: #5A5A5A; }"   # dark grey
        # "{ alternate-background-color: #FFF76B; background-color: #0B2E40; }" # Yellow on Dark Indign
        # "{ alternate-background-color: white; background-color: #0B2E40; }"   # Dark Indigo
        # "{ alternate-background-color: white; background-color: #OC374D; }"   # "Darker Indigo"
        # "{ alternate-background-color: white; background-color: #3C6478; }"   # "Lighter Indigo"
        # "{ alternate-background-color: #CADCFC; background-color: #00246B; }" # light blue on dark blue
        # "{ alternate-background-color: white; background-color: #AD2A1A; }"   # "Darker Ruby"
        # "{ alternate-background-color: white; background-color: #AD2A1A; }"   # "Darker Ruby"
        # "{ alternate-background-color: white; background-color: #527C27; }"   # "Darkest Kelly Green"
        # "{ alternate-background-color: white; background-color: #304616; }"   # light gray on dark Kelly Green"
        # "{ alternate-background-color: white; background-color: black; }"     # as boring as possible
        # "{ alternate-background-color: black; background-color: white; }"     # as boring as possible
        # "{ alternate-background-color: yellow; background-color: red; }"      # eye strain

        # Use an f-string to build the QSS string
        style_string = f"""
            QTableWidget {{
                background-color: {background_color};
                alternate-background-color: {alternate_color};
            }}
            QHeaderView::section {{
                background-color: {header_color};
                color: {text_color};
                font-size: 14pt;
            }}
            """

        self.setWindowTitle('Table Example')
        self.setGeometry(200, 200, 600, 400)
        
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        dlg_btn = QDialogButtonBox.StandardButton.Ok
        # Or use the close button
        # dlg_btn = QDialogButtonBox.StandardButton.Close
        self.ok_btn = QDialogButtonBox(dlg_btn)
        # self.ok_btn.accepted.connect(self.accept)
        self.ok_btn.accepted.connect(self.button_clicked)

        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setFont(QFont(fontname, fontsize))
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet(style_string)                
        
        self.table.setHorizontalHeaderLabels(['Country', 'Capital'])
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

    def button_clicked(self):
        # close dialog box
        self.close()

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

        # add menu bar, toolbar and QLabel 
        self.init_menu_bar()
        self.init_tool_bar()
        self.label_text = QLabel()
        self.label_text.setFont(QFont('Georgia', 20))
        self.label_text.setText('Hello.')
        self.layout.addWidget(self.label_text)

    def init_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        quit_action = QAction('Quit', self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)


    def init_tool_bar(self):
        QDir.addSearchPath('icon', './icons/')
        # usage: icon = QtGui.QIcon('icon:myicon.png')

        toolbar = QToolBar('Tools', self)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)
        toolbar.setIconSize(QSize(42, 42))  # Adjust icon size as needed 
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        
        # Its a cheesy generic name... tbb = Tool Bar Button 
        # Add 4 example buttons and bad jokes
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
        
        toolbar.addSeparator()
        self.check_bx = QAction(QIcon("icon:CheckOn.svg"), "another checkbox", self)
        self.check_bx.setCheckable(True)
        self.check_bx.setStatusTip("Any Wodka?")
        self.check_bx.triggered.connect(self.checkbox_state)
        # the event method seems to work ok
        # so why use style sheet? maybe if I have a lot of 
        # stuff?!? IDK
        # Stylesheet code to change the icon based on state.
        # I don't think I need to size the indicator
        #     QCheckBox::indicator {
        #         width: 20px;
        #         height: 20px;
        #     }  
        # checkbox_style = """
        #     QCheckBox::indicator:unchecked {
        #         image: url('./icons/Checkov.svg');
        #     }
        #     QCheckBox::indicator:checked {
        #         image: url('./icons/CheckOn.svg');
        #     }
        #     """
        # Any Trek fans out there? LOL
                    
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
        # update a QLabel with string passed in
        self.label_text.setText(bad_joke)
        self.label_text.adjustSize()
        self.layout.update()
    
    def checkbox_state(self):
        # Change the checkbox icon depending on its state.
        activated = self.check_bx.isChecked()
        if activated:
            self.check_bx.setIcon(QIcon('icon:checkov.svg'))
            self.layout.update()
        if not activated:
            self.check_bx.setIcon(QIcon('icon:checkOn.svg'))
            self.layout.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
