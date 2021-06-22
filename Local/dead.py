        # self.tagsSelector = QComboBox(self)
        # self.tagsList = []
        # self.tagsSelector(200, 150, 120, 40)
        # for i in PROBLEM_TAGS:
        #     temp = QCheckBox()
        #     self.tagsList.append(temp)


  
        # # adding items to combo box
        # combo_box.addItem("Geek")
        # combo_box.addItem("Super Geek")
        # combo_box.addItem("Ultra Geek")



        
    def fileSaveAs(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", 
                             "Text documents (*.txt);All files (*.*)")
        if not path:
            return
        self.fileSaveToPath(path)