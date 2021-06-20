from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainPage import mainScreen
import sys, os
import qdarkstyle
from qdarkstyle.dark.palette import DarkPalette
from Templates.Python.highlight import PythonHighlighter


directoryPath = os.getcwd()
App = QApplication(sys.argv)
App.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
QtGui.QFontDatabase.addApplicationFont(os.path.join(directoryPath, "Fonts", "FiraCodeL.ttf"))
QtGui.QFontDatabase.addApplicationFont(os.path.join(directoryPath, "Fonts", "monoL.ttf"))
window = mainScreen(App)
highlight = PythonHighlighter(window.editorScreen.document())
sys.exit(App.exec_())