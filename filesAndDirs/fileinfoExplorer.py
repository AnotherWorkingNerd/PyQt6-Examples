# from https://stackoverflow.com/questions/72155657/mouseclick-event-on-pyqt-folder-tree
# this was to work out using the mouse with a file picker but then morphed into a
# FileInfo thing with QFileSystemModel and Qmessagebox

import sys
from PyQt6.QtWidgets import  QMainWindow, QApplication, QHBoxLayout,QWidget, QVBoxLayout, QTreeView, QLineEdit, QMessageBox
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import Qt, QEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        application = App()
        layout.addWidget(application)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.perms = ''

    def initUI(self):
        self.model = QFileSystemModel()
        self.model.setNameFilters([''])
        self.model.setNameFilterDisables(0)
        # self.model.setRootPath('')
        self.model.setRootPath('/Users/gregm/src')

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        self.tree.setSortingEnabled(True)

        self.tree.clicked.connect(self.handle_clicked)
        # self.tree.clicked.connect(self.mousePressEvent)

        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        self.input = QLineEdit()
        layout.addWidget(self.input)
        self.setLayout(layout)
        self.show()

    def handle_clicked(self, index):
        filename = self.model.fileName(index)
        path = self.model.filePath(index)
        fileinfo = self.model.fileInfo(index)
        print(f'filename: {filename}, path: {path}, fileinfo {fileinfo.__dict__ }')
        # the message box works well but really unneeded here
        # require  PyQt6.QtWidgets import QMessageBox
        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Icon.Information)
        # msg.setWindowTitle('Item Details')
        # msgbox_text = f'filename: {filename} \npath: {path}\n file info {fileinfo.canonicalPath()}'
        # msg.setText(msgbox_text)
        # msg.exec()

        # these are all document at https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qfileinfo.html
        print(f'isSymLink: {fileinfo.isSymLink()}')
        print(f'symLinkTarget: {fileinfo.symLinkTarget()}')
        print(f'absoluteDir: {repr(fileinfo.absoluteDir())}')
        print(f'absoluteFilePath: {fileinfo.absoluteFilePath()}')       # this may include .. or . whereas canonicalFilePath does not.
        print(f'absolutePath: {fileinfo.absolutePath()}')
        print(f'basename: {fileinfo.baseName()}')                       # all characters in the file up to (but not including) the first ‘.’ character. so .bashrc is just '.'
        print(f'filename: {fileinfo.fileName()}')                        # Returns the name of the file system entry excluding path. so maybe better choice than the others.
        print(f'canonicalFilePath: {fileinfo.canonicalFilePath()}')   # I think this is the best choice for file path
        print(f'canonicalPath: {fileinfo.canonicalPath()}')
        print(f'completeBaseName: {fileinfo.completeBaseName()}')    # I think this is may NOT the best choice for basename. Same prob as .basename() above
        print(f'completeSuffix: {fileinfo.completeSuffix()}')
        print(f'dir: {fileinfo.dir()}')
        print(f'exists: {fileinfo.exists()}')
        print(f'path: {fileinfo.path()}')
        print(f'size: {fileinfo.size()}')
        print(f'stat: {fileinfo.stat()}')
        # need to figure out proper syntax.
        # print(f'fileTime: {fileinfo.fileTime(self.filetime )}')
        print(f'birthTime: {fileinfo.birthTime()}')
        print(f'lastModified: {fileinfo.lastModified()}')
        print(f'lastRead: {fileinfo.lastRead()}')
        print(f'metadataChangeTime: {fileinfo.metadataChangeTime()}')
        print(f'isAbsolute (path): {fileinfo.isAbsolute()}')
        print(f'isDir: {fileinfo.isDir()}')
        print(f'isExecutable: {fileinfo.isExecutable()}')
        print(f'isFile: {fileinfo.isFile()}')

        print(f'isReadable: {fileinfo.isReadable()}')
        print(f'isRelative: {fileinfo.isRelative()}')
        print(f'isRoot: {fileinfo.isRoot()}')
        print(f'isWritable: {fileinfo.isWritable()}')

        print(f'isAlias (macOS only): {fileinfo.isAlias()}')
        print(f'isbundle (macOS only): {fileinfo.isBundle()}')

        print(f'owner: {fileinfo.owner()}')
        print(f'ownerId: {fileinfo.ownerId()}')
        print(f'group: {fileinfo.group()}')
        print(f'groupId: {fileinfo.groupId()}')
        print('='*30)

        # permissions may take more work to figure out..
        # print(f'permission: {fileinfo.permission()}')
        # if fileinfo.permission(QFile.isWritable and  QFile.isReadable):
        #     print(f'This is user readable and witeable')


if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = MainWindow()
  w.show()
  app.exec()
