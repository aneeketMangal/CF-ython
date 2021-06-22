from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import qdarkstyle
from qdarkstyle.dark.palette import DarkPalette
import os
import qtawesome as qta
from Templates.Python.editor import CodeEditor
import syntax

class UiComponents():
    def __init__(self):
        font1 = QFontDatabase.applicationFontFamilies(0)[0]
        font2 = QFontDatabase.applicationFontFamilies(1)[0]
        if sys.platform == "linux" or sys.platform == "linux2":
            self.fixedfont = QFont(font1, 16)
        else:
            self.fixedfont = QFont(font1, 12)
        # self.fixedfont.setPointSize(16)
        self.fixedfont2 = QFont(font2, 16)
        # self.fixedfont2.setPointSize(16)
        

    def operationTile(self, name):
        button = QPushButton()
        button.setText(name)
        button.setFont(QFont('Times', 30))
        
        button.setFixedHeight(40)
        button.setFixedWidth(40)
        return button
        
    def buttonTile(self, name, height, width):
        button = QPushButton()
        button.setText(name)
        button.setFont(QFont('Times', 30))
        button.setFixedHeight(height)
        button.setFixedWidth(width)
        return button
    # def labelTile2(self, name, height, width)

    def labelTile(self, labelName, height, width, isBorder, isCenter = 1):
        temp = QLabel()
        temp.setText(labelName)
        temp.setFont(self.fixedfont)
        temp.setFixedHeight(height)
        temp.setFixedWidth(width)
        if (isBorder):
            temp.setStyleSheet("border :1px solid white;")
        if(isCenter):
            temp.setAlignment(QtCore.Qt.AlignCenter)
        return temp
    
    def labelTile2(self, labelName, height, width, color):
        temp = QLabel()
        temp.setText(labelName)
        temp.setFont(self.fixedfont)
        temp.setFixedHeight(height)
        temp.setFixedWidth(width)
        
        temp.setStyleSheet("background-color:" +color+";")
        temp.setAlignment(QtCore.Qt.AlignCenter)
        return temp

    def buttonTile2(self, labelName, height, width, color = "black"):
        temp = QPushButton()
        temp.setText(labelName)
        temp.setFont(self.fixedfont)
        temp.setFixedHeight(height)
        temp.setFixedWidth(width)
        temp.setStyleSheet("border :1px solid white;"+"background-color:" +color+";")
        return temp

    def info(self):
        self.infoScroll = QScrollArea()
        self.displayWidget3 = QGroupBox()
        self.info_grid = QGridLayout()
        count = 0
        self.infoTable = []
        for i in range(30):
            temp = self.labelTile("",100,120,False)
            temp.setAlignment(QtCore.Qt.AlignLeft)
            temp.setWordWrap(True)
            self.info_grid.addWidget(temp,count,0)
            tempp = self.labelTile("",100,800,False)
            tempp.setAlignment(QtCore.Qt.AlignLeft)
            tempp.setWordWrap(True)
            self.info_grid.addWidget(tempp,count, 1)
            self.infoTable.append([temp, tempp])
            count+=1
            
        self.displayWidget3.setLayout(self.info_grid)
        self.infoScroll.setWidget(self.displayWidget3)
        self.infoScroll.setWidgetResizable(True)


    def lineEditTile(self):
        temp = QLineEdit("")
        temp.setValidator(QIntValidator())
        temp.setFixedHeight(40)
        temp.setFixedWidth(100)
        temp.setStyleSheet("border :1px solid white;")
        temp.setAlignment(QtCore.Qt.AlignCenter)
        return temp
    

    def controlBox(self):
        self.runMode()
        self.controlScroll = QScrollArea()
        self.displayWidget4 = QGroupBox()
        self.controlGrid = QGridLayout()
        self.controlTable = []
        controlsD = ["Pipelined", "Forwarding", "Machine Code", "Cache(I$)", "Cache(D$)", "Block(I$)", "Block(D$)", "Way(I$)", "Way(D$)", "Replacement(I$)","Replacement(D$)", "Branch Pre.", "Initial State"]
        for i in range(len(controlsD)):
            temp = self.labelTile(controlsD[i], 40, 200, 0, 0)
            self.controlGrid.addWidget(temp, i+1, 0)
        
        
        
            
        for i in range(6):
            temp = self.lineEditTile()
            self.controlGrid.addWidget(temp, i+4, 1)
            self.controlTable.append(temp)

        self.controlGrid.addWidget(self.k1, 1, 1)
        self.controlGrid.addWidget(self.k2, 2, 1)
        self.controlGrid.addWidget(self.k3, 3, 1)
        
        self.k7 = self.buttonTile2("LRU", 40, 100, "grey")
        # self.k7.addItems(["LRU", "FIFO", "Random", "NRU"])
        
        self.k8 = self.buttonTile2("LRU", 40, 100, "grey")
        self.k9 = self.buttonTile2("AT", 40, 100, "grey")
        
        self.k10 = self.buttonTile2("Taken", 40, 100, "grey")

        self.controlGrid.addWidget(self.k7, 10, 1)
        self.controlGrid.addWidget(self.k8, 11, 1)
        self.controlGrid.addWidget(self.k9, 12, 1)
        self.controlGrid.addWidget(self.k10, 13, 1)
        
            
        self.controlTable[0].setText("64")
        self.controlTable[1].setText("64")
        self.controlTable[2].setText("4")
        self.controlTable[3].setText("4")
        self.controlTable[4].setText("2")
        self.controlTable[5].setText("2")
            
        self.displayWidget4.setLayout(self.controlGrid)
        self.controlScroll.setWidget(self.displayWidget4)
        self.controlScroll.setWidgetResizable(True)
        
        
    def mainLabel(self):        
        main_label_image = QLabel()
        main_label_image_pixmap = QPixmap("Images/logo.png")
        main_label_image_pixmap = main_label_image_pixmap.scaled(300, 50)
        self.save_button = self.buttonTile("\U0001F4BE", 50, 40)
        self.compile_button = self.buttonTile("\U00002699", 50, 40)
        self.load_button = self.buttonTile("\U000021E9", 50, 40)
        self.step_button = self.buttonTile("\U000000BB", 50, 40)
        
        main_label_image.setPixmap(main_label_image_pixmap)
        main_label_hBox = QHBoxLayout()
        main_label_hBox.addWidget(main_label_image)
        
        # main_label_hBox.addWidget(self.compile_button)
        # main_label_hBox.addWidget(self.save_button)
        # main_label_hBox.addWidget(self.load_button)
        # main_label_hBox.addWidget(self.step_button)
        main_label_hBox.addSpacing(40)
        return main_label_hBox
    



    def developerInfo(self):
        self.about = QMessageBox()
        self.about.exec_()

    def problemTable():
        self.problemView = QTableView()
        
        
    def createMenuBar(self):
        self.menuBar =  QMenuBar(self)
        
        fileMenu = QMenu("&File", self)
        self.menuBar.addMenu(fileMenu)
        editMenu = self.menuBar.addMenu("&Edit")
        helpMenu = self.menuBar.addMenu("&Help")


        

    def editor(self, filePath):
        self.editorScreen = CodeEditor()
        self.editorScreen.setStyleSheet("background-color: '#282A36'")
        self.editorScreen.setFont(self.fixedfont2)
        self.path = filePath
        self.editorScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editorScreen.setFrameStyle(QFrame.NoFrame)

    def input(self, filePath):
        self.inputScreen = QPlainTextEdit()
        # self.inputScreen.load(QtCore.QUrl().fromLocalFile("in"))
        self.inputScreen.setStyleSheet("background-color: '#282A36'")
        self.inputScreen.setFont(self.fixedfont)
        # f = QFile("in")
        # f.open(QFile.ReadOnly|QFile.Text)
        # istream = QTextStream(f)
        # self.inputScreen.setHtml(istream.readAll())
        # f.close()
        # self.inputScreen.setHtml("in")
        self.path = filePath
        self.inputScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inputScreen.setFrameStyle(QFrame.NoFrame)

    def output(self, filePath):
        self.outputScreen = QPlainTextEdit()
        self.outputScreen.setStyleSheet("background-color: '#282A36'")
        self.outputScreen.setFont(self.fixedfont)
        self.path = filePath
        self.outputScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.outputScreen.setFrameStyle(QFrame.NoFrame)
        
   
    def tabbedView1(self):
        self.tabs1 = QTabWidget()
        self.tabs1.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabs1.setIconSize(QtCore.QSize(60, 60))
        self.tabs1.setStyleSheet("border:none")
        self.tab1 = self.scroll1
        self.tab2 = self.scroll
        self.tab3 = self.infoScroll
        self.tab4 = self.controlScroll
        self.tab5 = self.scroll5
        self.tab6 = self.table1
        self.tab7 = self.table2
        self.tab8 = self.statsScroll
        
        self.tabs1.addTab(self.tab4, QIcon("GUI/Images/controls.png"), "")
        self.tabs1.addTab(self.tab1, QIcon("GUI/Images/registers.png"), "")
        self.tabs1.addTab(self.tab2, QIcon("GUI/Images/memory.png"), "")
        self.tabs1.addTab(self.tab8, QIcon("GUI/Images/stats.png"), "")
        self.tabs1.addTab(self.tab3, QIcon("GUI/Images/cache.png"), "")
 
    def tabbedView2(self):
        self.tabs2 = QTabWidget()
        self.tabs2.setStyleSheet("border:none")
        self.tabMain2 = self.editorScroll
        self.tabs2.addTab(self.tabMain2, "Code")
