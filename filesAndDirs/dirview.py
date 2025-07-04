# Copyright (C) 2020 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import sys
from argparse import ArgumentParser, RawTextHelpFormatter

from PyQt6.QtWidgets import QApplication, QFileIconProvider, QScroller, QTreeView
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QDir

"""PyQt6 port of the widgets/itemviews/dirview example from Qt v6.x"""


if __name__ == "__main__":
    app = QApplication(sys.argv)

    name = "Dir View"
    argument_parser = ArgumentParser(description=name,
                                     formatter_class=RawTextHelpFormatter)
    argument_parser.add_argument("--no-custom", "-c", action="store_true",
                                 help="Set QFileSystemModel.DontUseCustomDirectoryIcons")
    argument_parser.add_argument("--no-watch", "-w", action="store_true",
                                 help="Set QFileSystemModel.DontWatch")
    argument_parser.add_argument("directory",
                                 help="The directory to start in.",
                                 nargs='?', type=str)
    options = argument_parser.parse_args()
    #root_path = options.directory
    root_path = '/Users/gregm/src'


    model = QFileSystemModel()
    icon_provider = QFileIconProvider()
    model.setIconProvider(icon_provider)
    model.setRootPath('/Users/gregm/src')
    if options.no_custom:
        model.setOption(QFileSystemModel.DontUseCustomDirectoryIcons)
    if options.no_watch:
        model.setOption(QFileSystemModel.DontWatchForChanges)
    tree = QTreeView()
    tree.setModel(model)
    if root_path:
        root_index = model.index(QDir.cleanPath(root_path))
        print (root_path)
        print(root_index)
        if root_index.isValid():
            print('root_index is valid')
            tree.setRootIndex(root_index)

    # Demonstrating look and feel features
    tree.setAnimated(False)
    tree.setIndentation(20)
    tree.setSortingEnabled(True)
    availableSize = tree.screen().availableGeometry().size()
    tree.resize(availableSize / 2)
    tree.setColumnWidth(0, int(tree.width() / 3))

    # Make it flickable on touchscreens
    QScroller.grabGesture(tree, QScroller.ScrollerGestureType.TouchGesture)

    tree.setWindowTitle(name)
    tree.show()

    sys.exit(app.exec())
