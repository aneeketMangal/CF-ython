from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import qdarkstyle
from qdarkstyle.dark.palette import DarkPalette
import os
import subprocess
from UiComponents import UiComponents


class mainScreen(QMainWindow, UiComponents):
    def __init__(self, App):
        super().__init__()
        self.App = App
        self.title = "Text"
        self.directoryPath = os.getcwd()
        self.currFilePath = os.path.join(self.directoryPath, "main.py")
        self.currFilePath1 = os.path.join(self.directoryPath, "in")
        self.currFilePath2 = os.path.join(self.directoryPath, "op")
        # self.iconName = 
        # self.splash = QSplashScreen(QPixmap(self.iconName), Qt.WindowStaysOnTopHint)
        self.initWindow()
        # QTimer.singleShot(3000, self.initWindow)
        # self.splash.show()


    def warningDialog(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()
  
    # def fileOpen(self):
    #     path, _ = QFileDialog.getOpenFileName(self, "Open file", "", 
    #                          "Text documents (*.txt);All files (*.*)")

    #     if path:
    #         try:
    #             with open(path, 'rU') as f:
    #                 text = f.read()
    #         except Exception as e:
    #             self.warningDialog(str(e))
    #         else:
    #             self.currFilePath = path
    #             self.editor.setPlainText(text)

    def fileOpen(self, path):
        try:
            with open(path, 'rU') as f:
                text = f.read()
                return text
        except Exception as e:
            self.warningDialog(str(e))



    def fileSave(self, filePath, obj):
        if filePath:
            # self.warningDialog("Saving")
            return self.fileSaveToPath(filePath, obj)
        return self.fileSaveAs()

    def fileSaveAs(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", 
                             "Text documents (*.txt);All files (*.*)")
        if not path:
            return
        self.fileSaveToPath(path)
  
    def fileSaveToPath(self, path, obj):
        text = obj.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)
        except Exception as e:
            self.warningDialog(str(e))

        else:
            self.currFilePath = path

    # def fileOpen(self):
    #     f = open(self.currFilePath, 'r')
    #     self.editorScreen.setPlainText(f.read())

    # def fileSave(self):
    #     text = self.editorScreen.toPlainText()
    #     f = open(self.currFilePath, 'w')
    #     f.write(text)

    def changeTheme(self):
        if self.currentTheme == "Dark Theme":
            self.currentTheme = "Light Theme"
            self.App.setStyleSheet("")
        else:
            self.currentTheme = "Dark Theme"
            self.App.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=DarkPalette))


    def connections(self):
        self.save_button.clicked.connect(lambda: self.fileSave())
        self.editorScreen.setPlainText(self.fileOpen(self.currFilePath))
        # self.inputScreen.setPlainText(self.fileOpen(self.currFilePath1))
        self.outputScreen.setPlainText(self.fileOpen(self.currFilePath2))
        self.compile_button.clicked.connect(lambda: self.compile())
        self.editorScreen.shortcut["Save"].activated.connect(lambda:self.fileSave())
        self.editorScreen.shortcut["Run"].activated.connect(lambda:self.compile())
        # self.editorScreen.focus_out.connect(lambda:self.check_input(Dialog14))
        # self.theme_button.sclicked.connect(lambda: self.changeTheme())


    def compile(self):
        self.fileSave(self.currFilePath,self.editorScreen)
        self.fileSave(self.currFilePath1, self.inputScreen)

        subprocesses = subprocess.Popen("python3 main.py<in>op", shell=True, stdout=subprocess.PIPE)
        subprocess_return = subprocesses.stdout.read()
        self.outputScreen.setPlainText(self.fileOpen(self.currFilePath2))


    def window(self):
        self.editor(self.currFilePath)
        self.input(self.currFilePath1)
        self.output(self.currFilePath2)
        self.createMenuBar()
        self.problemTable()
        # self.tabbedView1()
        # self.tabbedView2()
        # self.help = self.tabs1
        # self.feed = self.tabs2

    


    def initWindow(self):
        # self.splash.close()
        self.setWindowTitle(self.title)
        logo_label = self.mainLabel()

        self.window()
        self.connections()

        self.setMenuBar(self.menuBar)
        hbox = QHBoxLayout()
        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(self.inputScreen)
        splitter1.addWidget(self.outputScreen)
        splitter1.setSizes([100,100])
        splitter1.setStyleSheet("background-color: transparent")
        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(self.editorScreen)
        splitter2.addWidget(splitter1)
        splitter2.setSizes([300,100])
        splitter2.setStyleSheet("background-color: transparent")

        hbox.addWidget(splitter2)

        vbox = QVBoxLayout()
        vbox.addLayout(logo_label, 1)
        vbox.addLayout(hbox, 20)
        temp = QWidget()
        temp.setLayout(vbox)
        self.setCentralWidget(temp)

        self.showMaximized()
