from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, os
import qdarkstyle
from globals.variables import *
import subprocess
from Templates.Python.editor import CodeEditor
from Templates.Python.highlight import PythonHighlighter
import requests
import json
import random
import webbrowser
import re
from bs4 import BeautifulSoup
