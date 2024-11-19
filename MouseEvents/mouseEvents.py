# Mouse events
# These are PyQt6 mouse events
#
# This started with the code from https://www.youtube.com/watch?v=8drZhYQSI34
# and has since been changed and massivly expanded upon.
# Maybe I got a bit carried away. Just call me Micky. :-D

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPointingDevice
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Move the mouse a bit then \nClick in this window\n\n \
                        since the Release Event happens after \n\
                        every button press\n \
                        everything is echoed to STDOUT.\n")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        self.label.setText("mouseMoveEvent")
        print('mouse event: move')

    def mouseReleaseEvent(self, event):
        self.label.setText("mouseReleaseEvent")
        print('mouse event: release button')

    def mousePressEvent(self, event):
        self.label.setText("mousePressEvent")
        print('mouse event: single click')
        mousePos = f" Pos: {event.pos().x()}, {event.pos().y()}"
        # OK a button was pressed. Which one?
        # since thses events happen pretty fast and be hard to see
        # they are also printed
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("Left mouse button pressed." + mousePos)
            print("Left mouse button pressed." + mousePos)
        if event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("Middle mouse button pressed." + mousePos)
            print("Middle mouse button pressed." + mousePos)
        if event.button() == Qt.MouseButton.RightButton:
            self.label.setText("Right mouse button pressed. " )
            print("Right mouse button pressed." + mousePos)
            device_info = self.get_device_info()
            self.label.setText(device_info)
            print(device_info)

        # MouseEventCreatedDoubleClick: This flag indicates that the
        # mouse event was created as part of a double-click action
        # and this flag helps differentiate between Single and
        # Double click events. It is only here for example purposes
        #
        # Using mouseDoubleClickEvent() (below) is the recommended
        # way. It is simpler, more Pythonic, and the preferred way to
        # handle double-clicks
        #
        # The other ways is:
        # if Qt.MouseEventFlag.MouseEventCreatedDoubleClick in event.flags():
        #     self.label.setText("Double-click detected!")
        # else:
        #     self.label.setText("Single click detected!")

    def mouseDoubleClickEvent(self, event):
        # Using mouseDoubleClickEvent() is the recommended
        # and the preferred way to handle double-clicks
        # It is simpler, more Pythonic, and cleaner.
        self.label.setText("mouseDoubleClickEvent")
        print('mouse event: double Click')

    def wheelEvent(self, event):
        # Detect mouse wheel rolling and direction.
        self.label.setText("Wheel Event - see stdout.")

        # Since many mice have 2 scroll wheels, usually one on the top
        # of mouse for vertical movement and a second wheel, usually on
        # the side of the mouse for horizontal movement.
        # Of course the configuration and location of the wheel can change
        # so YMMV but this will still pick up 2 distinct mouse wheel events.
        #
        # Get wheel delta. e.g how much roll in 1/8 degree increments.
        angle_delta = event.angleDelta()  # Returns a QPoint
        horizontal_scroll = angle_delta.x()    # Horizontal scroll amount
        vertical_scroll = angle_delta.y()      # Vertical scroll amount

        if abs(horizontal_scroll) > abs(vertical_scroll):
            horizOrVert = "Horizontal"
            scroll_amount = horizontal_scroll
        else:
            horizOrVert = "Vertical"
            scroll_amount = vertical_scroll

        if angle_delta.y() > 0:
            direction = "Scrolled Up"
        else:
            direction = "Scrolled Down"

        print(f"Wheel roll Detected.")
        print(f"Direction: {direction}")
        print(f"Axis      : {horizOrVert}")
        print(f"Scroll Amount: {scroll_amount} (in 1/8th degrees)")

    def get_device_info(self):
        # Retrieve and format information about the pointing device.
        device = QPointingDevice()
        if device is None:
            return "No pointing device detected."
        # get registered devices
        rDevs = device.devices()

        # I would expect there is a way to get information about the attached devices
        # but I can't figure it out without a lot of code to get very minimal info.
        # I read through the QPointingDevice and QInputDevice Class docs but
        # still don't get it. It's not for lack of trying.
        # just as an FYI. much of this returned zero or nothing.
        info = [
        #     # f"Device Type: {device.type().name} or type:{device.type()} \n",
        #     f"Device Type: {device.name()} or type:{device.pointerType()} \n",
        #     # f"Name: {device.name()}\n",
        #     f"Name: {type(device.Capability)}\n",
        #     f"Number of Buttons: {device.buttonCount()}\n",
        #     # f"Capabilities: {', '.join([cap.name for cap in device.capabilities()])}\n",
        #     f"Capabilities: { repr(device.capabilities().name)}\n",
        #     # f"Capabilities: { repr(device.Capability)}\n",
        #     # f"Pointer Type: {device.pointerType().name if hasattr(device, 'pointerType') else 'Unknown'}\n"
        #      f"Pointer Type: {device.pointerType().name }\n"
        #     f"Pointer Type: {device.pointerType().value}\n",
            f"There are {len(rDevs):d} registered input devices"
        ]
        return "\n".join(info)

if __name__ == "__main__":
# yea, I know I don't need this but I use it as
# a break from the rest of the the rest of the script

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()

    app.exec()
