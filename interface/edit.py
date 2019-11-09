from PyQt5          import QtWidgets as Qtw
from PyQt5.QtCore   import pyqtSignal, Qt
from PyQt5          import QtCore

from interface.ui   import editForm

class EditForm(Qtw.QMainWindow, editForm.Ui_editForm):
    """ Открывает диалоговое окно для заполнения tenderMethodsNames..
        
        Keyword arguments:
            methodNames -> ссылка на список способов закупок
        
    """
    params = pyqtSignal(object) # передача аргументов обратно в settings
    def __init__(self, data, flag=False, title='Новый элемент'):
        super().__init__()
        self.setWindowModality(Qt.ApplicationModal)
        if flag:
            self.methodNames = data['categories']
        else:
            self.methodNames = data['tenderMethodNames']
        self.setupUi(self, title)

        self.btn_pushTotree.clicked.connect(self.addItem)
        self.lineEdit.textChanged.connect(self.lineEvent)
        self.listTenderMethods.clicked.connect(self.listEvent)
        self.btn_removeFromtree.clicked.connect(self.delItem)
        self.pushButton.clicked.connect(self.__save)

        self.updateItems()

    def __save(self):
        """ отправляет сигнаал в DocumentsTab о сохранении. """
        self.params.emit(1)
        self.hide()

    def updateItems(self):
        """ Обновляет список. """
        lists = self.listTenderMethods
        lists.clear()
        self.methodNames.sort()
        lists.addItems(self.methodNames)
            
    def addItem(self):
        """ Добавляет новый item в список. """
        lists = self.listTenderMethods
        line = self.lineEdit
        text = line.text().strip()

        search = lists.findItems( text, QtCore.Qt.MatchFixedString )

        if not search:
            lists.addItem(text)
            self.methodNames.append(text)

        line.clear()
        self.updateItems()

    def lineEvent(self):
        """ Переключает видимость кнопок. """  
        text = self.lineEdit.text()

        if not text.strip() == "":
            self.btn_pushTotree.setEnabled(True)
        else:
            self.btn_pushTotree.setEnabled(False)

    def listEvent(self):
        """ Включает кнопку удаления. """    
        self.btn_removeFromtree.setEnabled(True)

    def delItem(self):
        """ Удаляет item из списка. """
        lists = self.listTenderMethods

        try:
            currentName = lists.currentItem().text()

            lists.takeItem( lists.currentRow() )
            if self.methodNames.count(currentName):
                self.methodNames.remove(currentName)
        except AttributeError:
            pass

    def keyPressEvent(self, event):            
        key_enter = QtCore.Qt.Key_Enter -1
        if event.key() == key_enter:
            text = self.lineEdit.text()
            if not text.strip() == "":
                self.addItem()

        if event.key() == QtCore.Qt.Key_Down:
            lists = self.listTenderMethods
            lists.setFocus()
            lists.setCurrentRow(0)
            self.listEvent()

        if event.key() == QtCore.Qt.Key_Up:
            self.lineEdit.setFocus()

        if event.key() == QtCore.Qt.Key_Delete:
            self.delItem()

        if event.key() == QtCore.Qt.Key_Escape:
            self.params.emit(1)
            self.hide()
            event.accept()
        

    def closeEvent(self, event):
        self.params.emit(1)
        self.hide()
        event.accept()