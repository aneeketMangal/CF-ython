from imports import *

class UiComponents():
    def __init__(self):
        font1 = QFontDatabase.applicationFontFamilies(0)[0]
        font2 = QFontDatabase.applicationFontFamilies(1)[0]
        if sys.platform == "linux" or sys.platform == "linux2":
            self.fixedfont = QFont(font1, 16)
        else:
            self.fixedfont = QFont(font1, 12)
        self.fixedfont2 = QFont(font2, 16)
        
    def buttonTile(self, name, height, width):
        button = QPushButton()
        button.setText(name)
        button.setFont(QFont('Times', 30))
        button.setFixedHeight(height)
        button.setFixedWidth(width)
        return button

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

    def lineEditTile(self):
        temp = QLineEdit("")
        temp.setValidator(QIntValidator())
        temp.setFixedHeight(40)
        temp.setFixedWidth(100)
        temp.setStyleSheet("border :1px solid white;")
        temp.setAlignment(QtCore.Qt.AlignCenter)
        return temp

        
    def mainLabel(self):        
        logo = QLabel()
        logoPixmap = QPixmap("Images/logo.png")
        logoPixmap = logoPixmap.scaled(300, 50)
        self.save_button = self.buttonTile("\U0001F4BE", 50, 40)
        self.compile_button = self.buttonTile("\U00002699", 50, 40)
        self.lowRange = self.lineEditTile()
        self.upRange = self.lineEditTile()
        self.search_button = self.buttonTile("\U0001F50D", 50, 40)
        logo.setPixmap(logoPixmap)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(logo)
        hbox2.addWidget(self.lowRange)
        hbox2.addWidget(self.upRange)
        hbox2.addWidget(self.search_button)
        hbox2.addWidget(self.compile_button)
        hbox2.addWidget(self.save_button)
        hbox2.addSpacing(40)
        return hbox2

    def problemTable(self):
        self.problemView = QTableWidget()
        self.problemView.setColumnCount(3)
        self.problemView.setHorizontalHeaderLabels(PROBLEM_VIEW_LABELS)
        header = self.problemView.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)


    def problemViewer(self):
        self.problemWidget = CodeEditor()
    def editor(self, filePath):
        self.editorScreen = CodeEditor()
        self.editorScreen.setStyleSheet("background-color: '#282A36'")
        self.editorScreen.setFont(self.fixedfont2)
        self.path = filePath
        self.editorScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editorScreen.setFrameStyle(QFrame.NoFrame)

    def input(self, filePath):
        self.inputScreen = QTextEdit()
        self.inputScreen.setStyleSheet("background-color: '#282A36'")
        self.inputScreen.setFont(self.fixedfont)
        self.path = filePath
        self.inputScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inputScreen.setFrameStyle(QFrame.NoFrame)

    def output(self, filePath):
        self.outputScreen = QTextEdit()
        self.outputScreen.setStyleSheet("background-color: '#282A36'")
        self.outputScreen.setFont(self.fixedfont)
        self.path = filePath
        self.outputScreen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.outputScreen.setFrameStyle(QFrame.NoFrame)
    
    def tabbedView2(self):
        self.tabs2 = QTabWidget()
        self.tabs2.setStyleSheet("border:none")
        self.tabMain1 = self.editorScreen
        self.tabs2.addTab(self.tabMain1, "Code")
        self.tabMain2 = self.problemWidget
        self.tabs2.addTab(self.tabMain2, "Statement")
