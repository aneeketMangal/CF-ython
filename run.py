from imports import *
from main import mainScreen
from UiComponents import UiComponents


directoryPath = os.getcwd()
print("Wait while the program loads.....................\nUsually it takes 20-30 seconds")
App = QApplication(sys.argv)
App.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
QFontDatabase.addApplicationFont(os.path.join(directoryPath, "Fonts", "FiraCodeL.ttf"))
QFontDatabase.addApplicationFont(os.path.join(directoryPath, "Fonts", "signikaL.ttf"))
window = mainScreen(App)
highlight = PythonHighlighter(window.editorScreen.document())
sys.exit(App.exec_())