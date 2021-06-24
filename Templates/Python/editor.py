from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QObject, Qt, QSize, QRect
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
# import numpy as np

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.myeditor = editor

    def sizeHint(self):
        return QSize(int(self.editor.lineNumberAreaWidth()), 0)

    def paintEvent(self, event):
        self.myeditor.lineNumberAreaPaintEvent(event)


class CodeEditor(QPlainTextEdit, QThread):
    def __init__(self):
        super().__init__()
        self.setDocumentTitle("temp")
        self.lineNumberArea = LineNumberArea(self)
        self.currTab = 0
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        # self.textChanged.connect(self.checkTabSetting)
        self.updateLineNumberAreaWidth(0)
        self.shortcut = {
        "Save": QShortcut(QKeySequence('Ctrl+S'), self),
        "Run": QShortcut(QKeySequence('Ctrl+Shift+B'), self),
        "Tab": QShortcut(QKeySequence('Ctrl+T'), self),
        "Copy": QShortcut(QKeySequence('Ctrl+Shift+P'), self),
        "Enter": QShortcut(QKeySequence('Alt+Up'), self),
        "Comment": QShortcut(QKeySequence('ctrl+/'), self),
        "Bracket1":  QShortcut(QKeySequence('Shift+['), self),
        "Bracket2":  QShortcut(QKeySequence('Shift+9'), self),
        "Bracket3":  QShortcut(QKeySequence('['), self),
        "Bracket4":  QShortcut(QKeySequence('"'), self)
         }
        self.shortcut["Copy"].activated.connect(self.copyGivenLine)
        self.shortcut["Comment"].activated.connect(self.comment)
        self.shortcut["Bracket1"].activated.connect(self.bracket)
        # self.shortcut["Enter"].activated.connect(self.shiftLineUp)
        # self.returnPressed.activated.connect(self.checkTabSetting)


    def bracket(self, br):
        cur = self.textCursor()
        if(br == "{"):
            cur.insertText("{}")
        elif(br == "["):
            cur.insertText("[]")
        elif(br == "'"):
            cur.insertText("''")



    def comment(self):
        d = self.textCursor()
        start = d.selectionStart()
        end = d.selectionEnd()
        d.setPosition(start)
        g = d.blockNumber()
        d.setPosition(end, QTextCursor.KeepAnchor)
        g = d.blockNumber()-g
        d.setPosition(start,  QTextCursor.MoveAnchor)
        while(g>=0):
            c = d.block().text()
            if(len(c.strip()) == 0):
                g-=1
                d.movePosition(QTextCursor.NextBlock, QTextCursor.KeepAnchor)   
                continue
            if(c.strip()[0] == "#"):
                temp = c.find("#")
                temp+=1
                if(c[temp] == " "):
                    temp+=1
                cur = d
                cur.movePosition(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)   
                # cur.close()
                for i in range(temp):
                    cur.deleteChar()
            else:
                cur = d
                cur.movePosition(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
                cur.insertText('# ')
                # cur.close()

            d.movePosition(QTextCursor.NextBlock, QTextCursor.KeepAnchor)   
            g-=1
        # self.setTextCursor(cur)
        


    def copyGivenLine(self):
        c = self.textCursor().block()
        c = c.text()
        cur = self.textCursor()
        cur.movePosition(QTextCursor.EndOfLine, QTextCursor.MoveAnchor)
        self.setTextCursor(cur)
        cur.insertText('\n')
        cur.insertText(c)

    def shiftLineUp(self):
        c = self.textCursor().block()
        if(c.blockNumber() !=0):
            c = c.text()
            cur = self.textCursor()
            cur.movePosition(QTextCursor.PreviousBlock, QTextCursor.MoveAnchor)
            self.setTextCursor(cur)
            self.textCursor().block().setUserData(e)
            d = cur.block().text()
            # self.insertPlainText("Dfsa")
            print(c)
            print(d)
        # self.setTextCursor(cur)
        # cur.insertText('\n')


        # cur.insertText(c)

        # print(type(c))

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            return self.checkTabSetting()
        if event.key() in (Qt.Key_BraceLeft, Qt.Key_BracketLeft, Qt.Key_QuoteLeft):
            return self.bracket(chr(event.key()))

        super().keyPressEvent(event)


    def getLastLineTabs(self):
        tabCount = 0
        try:
            cur = self.textCursor().block().blockNumber()
            tb = self.document().findBlockByLineNumber(cur).text()

            while (tb[tabCount] == "\t"):
                tabCount+=1
            if(tb.strip()[-1] == ":"):
                tabCount+=1

            return tabCount
            

        except Exception as e:
            return 0
        
        

        
    def checkTabSettingS(self):
        cur = self.textCursor();
        temp = cur
        cur.movePosition(QTextCursor.PreviousCharacter,QTextCursor.KeepAnchor,1);
        a = cur.selectedText()
        cur = temp
        try:
            if(ord(a[0]) == 8233):
                tabCount = self.getLastLineTabs()
                cur.movePosition(QTextCursor.NextCharacter,QTextCursor.KeepAnchor,1);
                cur.insertText('\t'*tabCount)
                print(tabCount)
        except Exception as e:
            print(e)

    def checkTabSetting(self):
        cur = self.textCursor();
        tabCount = self.getLastLineTabs()
        cur.insertText('\n')
        cur.insertText('\t'*tabCount)
        


    def lineNumberAreaWidth(self):
        digits = 1
        count = max(1, self.blockCount())
        while count >= 10:
            count /= 10
            digits += 1
        space = self.fontMetrics().width('9') * digits
        return space


    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)


    def updateLineNumberArea(self, rect, dy):

        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(),
                       rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)



    def lineNumberAreaPaintEvent(self, event):
        mypainter = QPainter(self.lineNumberArea)
        mypainter.fillRect(event.rect(), QColor("transparent"))
        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()
        height = self.fontMetrics().height()
        while block.isValid() and (top <= event.rect().bottom()):
            if block.isVisible() and (bottom >= event.rect().top()):
                number = str(blockNumber + 1)
                mypainter.setPen(QColor("grey"))
                mypainter.drawText(0, top, self.lineNumberArea.width()-3, height,
                 Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1

    def resizeEvent(self, event):
        super().resizeEvent(event)

        cr = self.contentsRect();
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(),
                    self.lineNumberAreaWidth(), cr.height()))



    def highlightCurrentLine(self):
        extraSelections = []

        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)


