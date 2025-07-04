# Src: https://stackabuse.com/styling-pyqt6-applications-default-and-custom-qss-stylesheets/
#      https://coderslegacy.com/python/pyqt6-css-stylesheets/
# 
# PyQt works with default OS-based themes. This means that not specifying a theme 
# will give the application a different look on different systems.
# Your application will look different on a Windows 10 machine as opposed to 
# a Linux machine.

# There are many styles or themes that ship with PyQt, other than the default themes.

# The QStyleFactory object holds all the default system styles.
from PyQt6.QtWidgets import QStyleFactory
print(QStyleFactory.keys())

# To find out which default style is applied to an existing application, 
# you can access the objectName() via app.style():
import sys
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
print(app.style().objectName())

# Applying System Styles to PyQt6 Applications
# To change the default system style to another style we can use 
# the setStyle() method on the QApplication instance,
# with another style as an argument.
# Let's set the default style to Fusion in a small application:

import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
app = QApplication(sys.argv)

# Set the 'Fusion' system style
app.setStyle('Fusion')

# Create the parent Widget of the Widgets added to the layout
window = QWidget()

# Create the Vertical Box Layout Manager, setting the window as parent by passing it in the constructor.
layout = QVBoxLayout(window)

# Create the button Widgets we will add to the layout.
# Add the button Widgets to the VerticalBoxLayout
layout.addWidget(QPushButton('One'))
layout.addWidget(QPushButton('Two'))
layout.addWidget(QPushButton('Three'))
layout.addWidget(QPushButton('Four'))
layout.addWidget(QPushButton('Five'))

# Show the parent Widget
window.show()

# Launch the application
sys.exit(app.exec())

# Although these styles are really nice - you might have a different 
# vision for your application. Much the same way you can stylize 
# HTML pages - you can also stylize PyQt applications - inline and 
# through QSS Stylesheets.