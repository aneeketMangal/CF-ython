from imports import *
from UiComponents import UiComponents

class mainScreen(QMainWindow, UiComponents):
    def __init__(self, App):
        super().__init__()
        self.App = App
        self.cfApi = CfApi()
        self.title = "CF-ython"
        self.directoryPath = os.getcwd()
        self.appIcon = os.path.join(self.directoryPath, "Images", "logo.png")
        self.currFilePath = os.path.join(self.directoryPath, "Local", "main.py")
        self.inputFile = os.path.join(self.directoryPath,"Local", "in.txt")
        self.outputFile = os.path.join(self.directoryPath, "Local", "op.txt")
        self.initWindow()


    def dialog(self, s):
        temp = QMessageBox(self)
        temp.setText(s)
        temp.setIcon(QMessageBox.Information)
        temp.show()

    def fileOpen(self, path):
        try:
            with open(path, 'rU') as f:
                text = f.read()
                return text
        except Exception as e:
            self.warningDialog(str(e))



    def fileSave(self, filePath, obj):
        print(filePath)
        return self.fileSaveToPath(filePath, obj)
  
    def fileSaveToPath(self, path, obj):
        text = obj.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)
        except Exception as e:
            self.warningDialog(str(e))



    def connections(self):
        self.save_button.clicked.connect(lambda: self.fileSave())
        self.editorScreen.setPlainText(self.fileOpen(self.currFilePath))
        self.inputScreen.setPlainText(self.fileOpen(self.inputFile))
        self.outputScreen.setPlainText(self.fileOpen(self.outputFile))
        self.compile_button.clicked.connect(lambda: self.compile())
        self.search_button.clicked.connect(lambda: self.loadCFProblems())
        # self.editorScreen.shortcut["Save"].activated.connect(lambda:self.fileSave())
        self.editorScreen.shortcut["Run"].activated.connect(lambda:self.compile())
        self.problemView.itemClicked.connect(self.openCFProblem)
        self.loadCFProblems()

    def compile(self):
        self.fileSave(self.currFilePath,self.editorScreen)
        # print(self.currFilePath)
        self.fileSave(self.inputFile, self.inputScreen)
        command = "python3 "+self.currFilePath+"<"+self.inputFile+">"+self.outputFile
        # print(command)
        subprocesses = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        subprocess_return = subprocesses.stdout.decode('utf8')
        print(subprocesses.stdout)
        self.outputScreen.setPlainText(self.fileOpen(self.outputFile))
        self.dialog("Look for errors on terminal")


    def window(self):
        self.editor(self.currFilePath)
        self.input(self.inputFile)
        self.output(self.outputFile)
        self.problemViewer()
        self.tabbedView2()
        self.problemTable()
    

    def loadCFProblems(self):
        a = self.lowRange.text()
        b = self.upRange.text()
        self.cfProblemSet = self.cfApi.getProblemsInRange(a, b)
        totalProblems = len(self.cfProblemSet)
        while (self.problemView.rowCount() > 0):
            self.problemView.removeRow(0)

        for i in range(len(self.cfProblemSet)):
            self.problemView.insertRow(i)
            self.problemView.setItem(i,0, QTableWidgetItem(str(self.cfProblemSet[i]['contestId'])+self.cfProblemSet[i]['index']))
            self.problemView.setItem(i,1, QTableWidgetItem(self.cfProblemSet[i]['name']))
            if('rating' in self.cfProblemSet[i]):
                self.problemView.setItem(i,2, QTableWidgetItem(str(self.cfProblemSet[i]['rating'])))

    def openCFProblem(self, cell):
        if(cell.column() == 0):
            self.cfApi.getProblemStatement(cell.text())

    def initWindow(self):
        self.header = self.mainLabel()
        self.window()
        self.connections()
        self.setWindowTitle(self.title)
        
        hbox = QHBoxLayout()
        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(self.inputScreen)
        splitter1.addWidget(self.outputScreen)
        splitter1.setSizes([100,100])
        splitter1.setStyleSheet("background-color: transparent")
        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(self.problemView)
        splitter2.addWidget(self.tabs2)
        splitter2.addWidget(splitter1)
        splitter2.setSizes([250, 350,100])
        splitter2.setStyleSheet("background-color: transparent")
        hbox.addWidget(splitter2)
        vbox = QVBoxLayout()
        vbox.addLayout(self.header, 1)
        vbox.addLayout(hbox, 20)
        temp = QWidget()
        temp.setLayout(vbox)
        self.setCentralWidget(temp)
        self.showMaximized()
