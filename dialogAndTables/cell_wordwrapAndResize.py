# another chatGPT example that doesn't quite work
# or at least not like I wanted.
from PyQt6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem,QHeaderView
)
from PyQt6.QtGui import QTextOption
from PyQt6.QtCore import Qt
import sys

class TableDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Dialog")
        self.resize(400, 300)  # Initial size of the dialog box

        # Create layout and QTableWidget
        layout = QVBoxLayout(self)
        table_widget = QTableWidget()

        # Configure QTableWidget
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(["Column 1", "Column 2"])
        table_widget.setRowCount(5)  # Add 5 rows

        # Set fixed size for Column 0 and stretchable size for Column 1
        table_widget.setColumnWidth(0, 20)
        # table_widget.horizontalHeader().setSectionResizeMode(0, QTableWidget.ResizeMode.Fixed)
        # table_widget.horizontalHeader().setSectionResizeMode(1, QTableWidget.ResizeMode.Stretch)
        table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        # Populate table with example data
        for row in range(5):
            item_col_0 = QTableWidgetItem(f"{row+1}")
            item_col_1 = QTableWidgetItem(f"This is a long text string that should wrap and adjust its width dynamically.")

            # Enable word wrapping for Column 1
            item_col_1.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            item_col_1.setFlags(item_col_1.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Make it read-only

            table_widget.setItem(row, 0, item_col_0)
            table_widget.setItem(row, 1, item_col_1)

        # Enable word wrapping for all cells in the table
        table_widget.setWordWrap(True)

        # Ensure the table fills the entire dialog box
        table_widget.setSizeAdjustPolicy(QTableWidget.SizeAdjustPolicy.AdjustToContents)
        table_widget.setMinimumSize(self.width(), self.height())

        # Add the table widget to the layout
        layout.addWidget(table_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = TableDialog()
    dialog.exec()
