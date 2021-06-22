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
from API.cf_api import CfApi
from globals.variables import *

class mainScreen(QMainWindow, UiComponents):
    def __init__(self, App):
        super().__init__()
        self.App = App
        self.cfApi = CfApi()
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
        self.search_button.clicked.connect(lambda: self.loadCFProblems())
        self.editorScreen.shortcut["Save"].activated.connect(lambda:self.fileSave())
        self.editorScreen.shortcut["Run"].activated.connect(lambda:self.compile())
        self.problemView.itemClicked.connect(self.openCFProblem)
        self.loadCFProblems()
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
        self.problemTable(MAX_PROBLEMS_TO_DISPLAY)
        # self.tabbedView1()
        # self.tabbedView2()
        # self.help = self.tabs1
        # self.feed = self.tabs2

    def loadCFProblems(self):
        a = self.lowRange.text()
        b = self.upRange.text()
        self.cfProblemSet = self.cfApi.getProblemsInRange(a, b)
        totalProblems = len(self.cfProblemSet)
        print(self.cfProblemSet[0])
        while (self.problemView.rowCount() > 0):
            self.problemView.removeRow(0)

        for i in range(len(self.cfProblemSet)):
            self.problemView.insertRow(i)
            self.problemView.setItem(i,0, QTableWidgetItem(str(self.cfProblemSet[i]['contestId'])+self.cfProblemSet[i]['index']))
            self.problemView.setItem(i,1, QTableWidgetItem(self.cfProblemSet[i]['name']))
            if('rating' in self.cfProblemSet[i]):
                self.problemView.setItem(i,2, QTableWidgetItem(str(self.cfProblemSet[i]['rating'])))
            # print(self.cfProblesmSet[i])
        pass

    def openCFProblem(self, cell):
        if(cell.column() == 0):
            print(cell.row(), cell.column(), cell.text())



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
        splitter2.addWidget(self.problemView)
        splitter2.addWidget(self.editorScreen)
        splitter2.addWidget(splitter1)
        splitter2.setSizes([250, 400,100])
        splitter2.setStyleSheet("background-color: transparent")

        hbox.addWidget(splitter2)

        vbox = QVBoxLayout()
        vbox.addLayout(logo_label, 1)
        vbox.addLayout(hbox, 20)
        temp = QWidget()
        temp.setLayout(vbox)
        self.setCentralWidget(temp)

        self.showMaximized()
