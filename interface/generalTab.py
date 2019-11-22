import re, sys, os, datetime

from PyQt5.QtWidgets        import QFileDialog
from PyQt5.QtWidgets        import QMessageBox
from PyQt5.QtCore           import pyqtSignal, Qt
from interface.variablesTab import VariablesTab
from interface.edit         import EditForm
from processing             import dbase

class GeneralTab(VariablesTab):
    params = pyqtSignal(object)
    def __init__(self, restoredData, localGeneral, setView=False):
        VariablesTab.__init__(self, restoredData, setView)
        self.setWindowModality(Qt.ApplicationModal)
        self.restoredData = restoredData
        self.lets = restoredData["variables"]['default']
        self.btn_save.clicked.connect(self._save)
        self.localGeneral = localGeneral
        self.generalInit() # __________вкладка основные__________
        self._update()

        self.checkBox_openfolder.clicked.connect(self.set_openfolder)
        self.checkBox_openpayment.clicked.connect(self.set_openpayment)
        self.sharedCheckBox.clicked.connect(self.trigger_shared_checkbox)
        self.SharedButton.clicked.connect(self.set_shared_path)
        self.onTopCheckBox.clicked.connect(self.set_windows_ontop)

        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def set_windows_ontop(self):
        if self.onTopCheckBox.isChecked():
            self.restoredData['general']['windowsOnTop'] = True
        else:
            self.restoredData['general']['windowsOnTop'] = False


    def set_shared_path(self):
        path = QFileDialog.getExistingDirectory(self, "text")
        if path:
            storage = '%s/storage' % path
            if os.path.exists(storage):
                self.restoredData['general']['shared'] = storage
                self.restoredData = dbase.read(storage)
                self.restoredData['general']['shared'] = storage
            else:
                self.restoredData['general']['shared'] = storage
                dbase.save(self.restoredData, storage)

            self._update()
            self.trigger_shared_checkbox()

    def trigger_shared_checkbox(self):
        if self.sharedCheckBox.checkState():
           self.sharedPathLine.setEnabled(True)
           self.SharedButton.setEnabled(True)
        else:
           self.sharedPathLine.setEnabled(False)
           self.SharedButton.setEnabled(False)
           self.restoredData['general']['shared'] = ''
        
    def _update(self):
        shared = self.restoredData['general']['shared']
        if shared:
            self.sharedCheckBox.setCheckState(2)
            self.sharedPathLine.setText(shared)
            self.sharedPathLine.setEnabled(True)
            self.SharedButton.setEnabled(True)
        
        winOnTop = self.restoredData['general']['windowsOnTop']
        if winOnTop:
            self.onTopCheckBox.setCheckState(2)

        self.comboDataSet()
        self._up_combo_tnd_method()

    def comboDataSet(self):
        self._catCombo.clear()
        self._catCombo.addItems(self.restoredData['categories'])

    def set_openpayment(self):
        checkbox = self.checkBox_openpayment.checkState()
        if checkbox:
            self.restoredData['general']['openpayment'] = True
        else:
            self.restoredData['general']['openpayment'] = False

    def set_openfolder(self):
        checkbox = self.checkBox_openfolder.checkState()
        if checkbox:
            self.restoredData['general']['openfolder'] = True
        else:
            self.restoredData['general']['openfolder'] = False

    def displayDesired(self, data):
        if data[0] == '44':
            print(44)
            self.radio_Law44.setChecked(True)
            self.law = 44
        else:
            print(223)
            self.law = 223
            self.radio_Law223.setChecked(True)
        self.innerUpdate(data[1])

    def _save(self):
        sheetName = self.sheetName.text().strip()
        self.restoredData['general']['sheetName'] = sheetName
        if self.validateCells():
            text = "Введите числовой номер ячейки!"
            QMessageBox.warning(self, 'Внимание!', text, QMessageBox.Ok)
            print("1111")
            self.tabWidget.setCurrentIndex(2)
        else:
            print("2")
            cellTopLeft = self.cellTopLeft.text().strip()
            self.restoredData['general']['cellTopLeft'] = cellTopLeft
            cellBotDn = self.cellBotDn.text().strip()
            self.restoredData['general']['cellBotDn'] = cellBotDn
            data = self.restoredData, self.localGeneral
            self.params.emit(data)
            self.hide()

    def validateCells(self):
        def reserch(cell):
            ru_symbols = re.search(r'[А-я]', cell)
            en_symbols = re.search(r'[A-z]', cell)
            other = re.search(r'\W', cell)
            if ru_symbols or en_symbols:
                return True
            if other:
                return True
            
        a = reserch( self.cellTopLeft.text() )
        b = reserch( self.cellBotDn.text() )

        if a or b:
            return True

    def closeEvent(self, event):
        data = self.restoredData, self.localGeneral
        self.params.emit(data)
        self.hide()
        event.accept()

    def generalInit(self):
        """ Вкладка основные."""

        def update():
            general = self.restoredData['general']
            self.projectspath.setText(self.localGeneral['mainPath'])
            self.paymentpath.setText(general['paymentPath'])
            self.sheetName.setText(general['sheetName'])
            self.cellTopLeft.setText(general['cellTopLeft'])
            self.cellBotDn.setText(general['cellBotDn'])
            checkbox_data_set()

        def checkbox_data_set():
            general = self.restoredData['general']
            if general['openfolder']:
                self.checkBox_openfolder.setChecked(True)
            else:
                self.checkBox_openfolder.setChecked(False)

            if general['openpayment']:
                self.checkBox_openpayment.setChecked(True)
            else:
                self.checkBox_openpayment.setChecked(False)


        def __signalHandler(signal):
            """ Получает сигнал из EditForm о сохранении. """
            if signal:
                self.setDisabled(False)
                comboDataSet()

        def __openEditForm():
            """ Открывает окно редактирования объекта {tenderMethodNames}. """
            self.setDisabled(True)
            self.form = EditForm(self.restoredData, 1, title='Новая категория')
            self.form.params.connect(__signalHandler)
            self.form.show()

        def comboDataSet():
            self._catCombo.clear()
            self._catCombo.addItems(self.restoredData['categories'])

        def choseProjectpath():
            text = r"Выберите основную папку проектов"
            path = QFileDialog.getExistingDirectory(self, text)
            if path:
                self.localGeneral['mainPath'] = path
            update()

        def chosePaymentpath():
            text = r"Выберите файл расчета"
            path = QFileDialog.getOpenFileName(self, text, '', r"Документы (*.xlsx)")
            print(path[0])
            if path[0]:
                self.restoredData['general']['paymentPath'] = path[0]
            update()

        self.btnProjectpath.clicked.connect(choseProjectpath)
        self.btnPaymentpath.clicked.connect(chosePaymentpath)
        self._catComboBtn.clicked.connect(__openEditForm)
        update()