# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.setEnabled(True)
        settings.resize(528, 651)
        self.centralwidget = QtWidgets.QWidget(settings)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(2, 0, 0, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_Law44 = QtWidgets.QRadioButton(self.tab)
        self.radio_Law44.setMinimumSize(QtCore.QSize(63, 0))
        self.radio_Law44.setObjectName("radio_Law44")
        self.horizontalLayout.addWidget(self.radio_Law44)
        self.radio_Law223 = QtWidgets.QRadioButton(self.tab)
        self.radio_Law223.setObjectName("radio_Law223")
        self.horizontalLayout.addWidget(self.radio_Law223)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.label_TendMethod = QtWidgets.QLabel(self.tab)
        self.label_TendMethod.setObjectName("label_TendMethod")
        self.gridLayout.addWidget(self.label_TendMethod, 2, 0, 1, 1)
        self.combo_tendMethod = QtWidgets.QComboBox(self.tab)
        self.combo_tendMethod.setMinimumSize(QtCore.QSize(210, 0))
        self.combo_tendMethod.setObjectName("combo_tendMethod")
        self.gridLayout.addWidget(self.combo_tendMethod, 3, 0, 1, 1)
        self.btn_tendMethod = QtWidgets.QPushButton(self.tab)
        self.btn_tendMethod.setMinimumSize(QtCore.QSize(105, 0))
        self.btn_tendMethod.setMaximumSize(QtCore.QSize(105, 16777215))
        self.btn_tendMethod.setObjectName("btn_tendMethod")
        self.gridLayout.addWidget(self.btn_tendMethod, 3, 1, 1, 1)
        self.label_Law = QtWidgets.QLabel(self.tab)
        self.label_Law.setObjectName("label_Law")
        self.gridLayout.addWidget(self.label_Law, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 18, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_pushTotree = QtWidgets.QPushButton(self.tab)
        self.btn_pushTotree.setEnabled(False)
        self.btn_pushTotree.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_pushTotree.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_pushTotree.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("interface/icons/add.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pushTotree.setIcon(icon)
        self.btn_pushTotree.setObjectName("btn_pushTotree")
        self.horizontalLayout_2.addWidget(self.btn_pushTotree)
        self.btn_removeFromtree = QtWidgets.QPushButton(self.tab)
        self.btn_removeFromtree.setEnabled(False)
        self.btn_removeFromtree.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_removeFromtree.setStyleSheet("background-color: rgba(255, 255, 255, 5);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("interface/icons/remove.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_removeFromtree.setIcon(icon1)
        self.btn_removeFromtree.setObjectName("btn_removeFromtree")
        self.horizontalLayout_2.addWidget(self.btn_removeFromtree)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.treeDocuments = QtWidgets.QTreeWidget(self.tab)
        self.treeDocuments.setMinimumSize(QtCore.QSize(437, 179))
        self.treeDocuments.setObjectName("treeDocuments")
        self.verticalLayout_3.addWidget(self.treeDocuments)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.choseAllCheckBox = QtWidgets.QCheckBox(self.tab)
        self.choseAllCheckBox.setEnabled(False)
        self.choseAllCheckBox.setObjectName("choseAllCheckBox")
        self.horizontalLayout_4.addWidget(self.choseAllCheckBox)
        self.btn_clear = QtWidgets.QPushButton(self.tab)
        self.btn_clear.setEnabled(False)
        self.btn_clear.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("interface/icons/clear.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear.setIcon(icon2)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_4.addWidget(self.btn_clear)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.word_editline = QtWidgets.QLineEdit(self.tab_4)
        self.word_editline.setObjectName("word_editline")
        self.gridLayout_3.addWidget(self.word_editline, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.word_value = QtWidgets.QTextEdit(self.tab_4)
        self.word_value.setMinimumSize(QtCore.QSize(0, 0))
        self.word_value.setMaximumSize(QtCore.QSize(16777215, 88))
        self.word_value.setObjectName("word_value")
        self.verticalLayout_6.addWidget(self.word_value)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(0, 13, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.word_btn_add = QtWidgets.QPushButton(self.tab_4)
        self.word_btn_add.setEnabled(False)
        self.word_btn_add.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.word_btn_add.setIcon(icon)
        self.word_btn_add.setObjectName("word_btn_add")
        self.horizontalLayout_10.addWidget(self.word_btn_add)
        self.word_btn_del = QtWidgets.QPushButton(self.tab_4)
        self.word_btn_del.setEnabled(False)
        self.word_btn_del.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.word_btn_del.setIcon(icon1)
        self.word_btn_del.setObjectName("word_btn_del")
        self.horizontalLayout_10.addWidget(self.word_btn_del)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.word_tree = QtWidgets.QTreeWidget(self.tab_4)
        self.word_tree.setObjectName("word_tree")
        item_0 = QtWidgets.QTreeWidgetItem(self.word_tree)
        self.verticalLayout_6.addWidget(self.word_tree)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_10.addWidget(self.label_5)
        self.excel_editline = QtWidgets.QLineEdit(self.tab_5)
        self.excel_editline.setObjectName("excel_editline")
        self.verticalLayout_10.addWidget(self.excel_editline)
        self.verticalLayout_8.addLayout(self.verticalLayout_10)
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.excel_value = QtWidgets.QTextEdit(self.tab_5)
        self.excel_value.setMinimumSize(QtCore.QSize(0, 0))
        self.excel_value.setMaximumSize(QtCore.QSize(16777215, 88))
        self.excel_value.setObjectName("excel_value")
        self.verticalLayout_8.addWidget(self.excel_value)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(0, 13, -1, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.btn_add_5 = QtWidgets.QPushButton(self.tab_5)
        self.btn_add_5.setEnabled(False)
        self.btn_add_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.btn_add_5.setIcon(icon)
        self.btn_add_5.setObjectName("btn_add_5")
        self.horizontalLayout_14.addWidget(self.btn_add_5)
        self.btn_del_5 = QtWidgets.QPushButton(self.tab_5)
        self.btn_del_5.setEnabled(False)
        self.btn_del_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.btn_del_5.setIcon(icon1)
        self.btn_del_5.setObjectName("btn_del_5")
        self.horizontalLayout_14.addWidget(self.btn_del_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        self.excel_tree = QtWidgets.QTreeWidget(self.tab_5)
        self.excel_tree.setObjectName("excel_tree")
        item_0 = QtWidgets.QTreeWidgetItem(self.excel_tree)
        self.verticalLayout_8.addWidget(self.excel_tree)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.default_tree = QtWidgets.QTreeWidget(self.tab_8)
        self.default_tree.setObjectName("default_tree")
        item_0 = QtWidgets.QTreeWidgetItem(self.default_tree)
        font = QtGui.QFont()
        font.setItalic(True)
        item_0.setFont(0, font)
        font = QtGui.QFont()
        font.setItalic(True)
        item_0.setFont(1, font)
        item_0.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.verticalLayout_14.addWidget(self.default_tree)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.verticalLayout_4.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self._catCombo = QtWidgets.QComboBox(self.groupBox)
        self._catCombo.setMinimumSize(QtCore.QSize(210, 0))
        self._catCombo.setObjectName("_catCombo")
        self.horizontalLayout_11.addWidget(self._catCombo)
        self._catComboBtn = QtWidgets.QPushButton(self.groupBox)
        self._catComboBtn.setMinimumSize(QtCore.QSize(105, 0))
        self._catComboBtn.setMaximumSize(QtCore.QSize(105, 16777215))
        self._catComboBtn.setObjectName("_catComboBtn")
        self.horizontalLayout_11.addWidget(self._catComboBtn)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.paymentpath = QtWidgets.QLineEdit(self.groupBox_2)
        self.paymentpath.setReadOnly(True)
        self.paymentpath.setObjectName("paymentpath")
        self.horizontalLayout_6.addWidget(self.paymentpath)
        self.btnPaymentpath = QtWidgets.QToolButton(self.groupBox_2)
        self.btnPaymentpath.setObjectName("btnPaymentpath")
        self.horizontalLayout_6.addWidget(self.btnPaymentpath)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_32.addWidget(self.label_13)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_32.addWidget(self.label_3)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_32.addWidget(self.label_17)
        self.verticalLayout_5.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.sheetName = QtWidgets.QLineEdit(self.groupBox_2)
        self.sheetName.setObjectName("sheetName")
        self.horizontalLayout_31.addWidget(self.sheetName)
        self.cellTopLeft = QtWidgets.QLineEdit(self.groupBox_2)
        self.cellTopLeft.setObjectName("cellTopLeft")
        self.horizontalLayout_31.addWidget(self.cellTopLeft)
        self.cellBotDn = QtWidgets.QLineEdit(self.groupBox_2)
        self.cellBotDn.setObjectName("cellBotDn")
        self.horizontalLayout_31.addWidget(self.cellBotDn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_31)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.projectspath = QtWidgets.QLineEdit(self.groupBox_3)
        self.projectspath.setReadOnly(True)
        self.projectspath.setObjectName("projectspath")
        self.horizontalLayout_5.addWidget(self.projectspath)
        self.btnProjectpath = QtWidgets.QToolButton(self.groupBox_3)
        self.btnProjectpath.setObjectName("btnProjectpath")
        self.horizontalLayout_5.addWidget(self.btnProjectpath)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_7.addWidget(self.label_18)
        self.treeProjectStruct = QtWidgets.QTreeWidget(self.groupBox_3)
        self.treeProjectStruct.setObjectName("treeProjectStruct")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeProjectStruct)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeProjectStruct)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeProjectStruct)
        self.verticalLayout_7.addWidget(self.treeProjectStruct)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox_openfolder = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_openfolder.setObjectName("checkBox_openfolder")
        self.horizontalLayout_12.addWidget(self.checkBox_openfolder)
        self.checkBox_openpayment = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_openpayment.setObjectName("checkBox_openpayment")
        self.horizontalLayout_12.addWidget(self.checkBox_openpayment)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SharedButton = QtWidgets.QToolButton(self.groupBox_5)
        self.SharedButton.setEnabled(False)
        self.SharedButton.setObjectName("SharedButton")
        self.gridLayout_2.addWidget(self.SharedButton, 1, 1, 1, 1)
        self.sharedPathLine = QtWidgets.QLineEdit(self.groupBox_5)
        self.sharedPathLine.setEnabled(False)
        self.sharedPathLine.setReadOnly(True)
        self.sharedPathLine.setObjectName("sharedPathLine")
        self.gridLayout_2.addWidget(self.sharedPathLine, 1, 0, 1, 1)
        self.sharedCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.sharedCheckBox.setObjectName("sharedCheckBox")
        self.gridLayout_2.addWidget(self.sharedCheckBox, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setMinimumSize(QtCore.QSize(105, 0))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_3.addWidget(self.btn_save)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(settings)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Настройки"))
        self.radio_Law44.setText(_translate("settings", "№ 44"))
        self.radio_Law223.setText(_translate("settings", "№ 223"))
        self.label_TendMethod.setText(_translate("settings", "Для способа закупки"))
        self.combo_tendMethod.setToolTip(_translate("settings", "<html><head/><body><p>Способ закупки</p></body></html>"))
        self.btn_tendMethod.setToolTip(_translate("settings", "<html><head/><body><p>Открыть окно редактирования списка способов закупок.</p></body></html>"))
        self.btn_tendMethod.setText(_translate("settings", "Редактировать"))
        self.label_Law.setText(_translate("settings", "Федеральный закон"))
        self.label.setText(_translate("settings", "Список документов"))
        self.btn_pushTotree.setText(_translate("settings", "Добавить"))
        self.btn_removeFromtree.setText(_translate("settings", "Удалить"))
        self.treeDocuments.setToolTip(_translate("settings", "<html><head/><body><p><span style=\" font-weight:600;\">Список документов</span> прикладываемых к текущему способу закупки, по выбранному закону. Установите флажок &quot;всегда прикладывать&quot; для повторяющихся в каждой заявке документов</p><p>например: Декларация СМП или Сведения об ИНН<br/></p></body></html>"))
        self.treeDocuments.headerItem().setText(0, _translate("settings", "Наименование"))
        self.treeDocuments.headerItem().setText(1, _translate("settings", "Дата создания"))
        self.treeDocuments.headerItem().setText(2, _translate("settings", "Всегда прикладывать"))
        self.choseAllCheckBox.setText(_translate("settings", "Пометить все"))
        self.btn_clear.setText(_translate("settings", "Отчистить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("settings", "Документы"))
        self.tabWidget_2.setToolTip(_translate("settings", "<html><head/><body><p/></body></html>"))
        self.word_editline.setToolTip(_translate("settings", "<html><head/><body><p><span style=\" font-weight:600;\">Имя переменной.</span> Программа будет искать данное значение в ваших документах. Придумаете оригинальное значение которое нигде больше не встречается.</p><p><span style=\" font-weight:600; color:#141c68;\">Пример переменной: </span><span style=\" font-weight:600; color:#ff530f;\">_ФИО_ </span></p></body></html>"))
        self.label_7.setToolTip(_translate("settings", "<html><head/><body><p/></body></html>"))
        self.label_7.setText(_translate("settings", "Переменная"))
        self.label_9.setToolTip(_translate("settings", "<html><head/><body><p/></body></html>"))
        self.label_9.setText(_translate("settings", "Значение"))
        self.word_value.setToolTip(_translate("settings", "<html><head/><body><p>Значение данного поля вставляется на место найденной в документе переменной</p></body></html>"))
        self.word_btn_add.setText(_translate("settings", "Добавить"))
        self.word_btn_del.setText(_translate("settings", "Удалить"))
        self.word_tree.setToolTip(_translate("settings", "<html><head/><body><p>Список всех переменных для документов в формате word 2010 и выше</p></body></html>"))
        self.word_tree.headerItem().setText(0, _translate("settings", "Переменная"))
        self.word_tree.headerItem().setText(1, _translate("settings", "Значение"))
        __sortingEnabled = self.word_tree.isSortingEnabled()
        self.word_tree.setSortingEnabled(False)
        self.word_tree.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("settings", "Word"))
        self.label_5.setToolTip(_translate("settings", "<html><head/><body><p/></body></html>"))
        self.label_5.setText(_translate("settings", "Переменная"))
        self.excel_editline.setToolTip(_translate("settings", "<html><head/><body><p><span style=\" font-weight:600;\">Имя переменной.</span> Программа будет искать данное значение в ваших документах. Придумаете оригинальное значение которое нигде больше не встречается.</p><p><span style=\" font-weight:600; color:#141c68;\">Пример переменной: </span><span style=\" font-weight:600; color:#ff530f;\">_НМЦК_ </span></p></body></html>"))
        self.label_4.setToolTip(_translate("settings", "<html><head/><body><p/></body></html>"))
        self.label_4.setText(_translate("settings", "Значение"))
        self.excel_value.setToolTip(_translate("settings", "<html><head/><body><p>Значение данного поля вставляется на место найденной в документе переменной</p></body></html>"))
        self.btn_add_5.setText(_translate("settings", "Добавить"))
        self.btn_del_5.setText(_translate("settings", "Удалить"))
        self.excel_tree.setToolTip(_translate("settings", "<html><head/><body><p>Список все переменных для документов Excel всех версий</p></body></html>"))
        self.excel_tree.headerItem().setText(0, _translate("settings", "Переменная"))
        self.excel_tree.headerItem().setText(1, _translate("settings", "Значение"))
        __sortingEnabled = self.excel_tree.isSortingEnabled()
        self.excel_tree.setSortingEnabled(False)
        self.excel_tree.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("settings", "Excel"))
        self.default_tree.setToolTip(_translate("settings", "<html><head/><body><p><span style=\" font-weight:600;\">Стандартные переменные</span> заменяются на значения полей основной формы.<br> Вставте нужную переменную обозначенную нижними подчеркиваними с обеих сторон <span style=\" color:#ff5500;\">_</span><span style=\" color:#07b607;\">ПЕРЕМЕННАЯ</span><span style=\" color:#ff5500;\">_<br/></span>в ваш документ <span style=\" font-weight:600;\">Excel </span>или <span style=\" font-weight:600;\">Word</span></p><p><span style=\" font-weight:600; color:#0a91d9;\">Двойной щелчек мыши для копирования</span></p></body></html>"))
        self.default_tree.headerItem().setText(0, _translate("settings", "Наименование"))
        self.default_tree.headerItem().setText(1, _translate("settings", "Переменная"))
        __sortingEnabled = self.default_tree.isSortingEnabled()
        self.default_tree.setSortingEnabled(False)
        self.default_tree.topLevelItem(0).setText(0, _translate("settings", "Дата"))
        self.default_tree.topLevelItem(0).setText(1, _translate("settings", "%ДАТА%"))
        self.default_tree.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("settings", "Стандартные"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("settings", "Переменные"))
        self.groupBox.setTitle(_translate("settings", "Категории товаров"))
        self._catCombo.setToolTip(_translate("settings", "<html><head/><body><p>Способ закупки</p></body></html>"))
        self._catComboBtn.setText(_translate("settings", "Редактировать"))
        self.groupBox_2.setTitle(_translate("settings", "Документ расчета xlsx"))
        self.btnPaymentpath.setText(_translate("settings", "..."))
        self.label_13.setText(_translate("settings", "Имя листа"))
        self.label_3.setText(_translate("settings", "Номер первой ячейки"))
        self.label_17.setText(_translate("settings", "Номер последней ячейки"))
        self.groupBox_3.setTitle(_translate("settings", "Структура проекта"))
        self.label_2.setText(_translate("settings", "Путь к папке с заявками"))
        self.btnProjectpath.setText(_translate("settings", "..."))
        self.label_18.setText(_translate("settings", "Настройка структуры"))
        self.treeProjectStruct.headerItem().setText(0, _translate("settings", "Корневая папка заявки"))
        __sortingEnabled = self.treeProjectStruct.isSortingEnabled()
        self.treeProjectStruct.setSortingEnabled(False)
        self.treeProjectStruct.topLevelItem(0).setText(0, _translate("settings", "./Заказчик"))
        self.treeProjectStruct.topLevelItem(1).setText(0, _translate("settings", "./Состав заявки"))
        self.treeProjectStruct.topLevelItem(1).child(0).setText(0, _translate("settings", "./WORD"))
        self.treeProjectStruct.topLevelItem(1).child(0).child(0).setText(0, _translate("settings", "Изменяемые документы"))
        self.treeProjectStruct.topLevelItem(1).child(1).setText(0, _translate("settings", "Документация"))
        self.treeProjectStruct.topLevelItem(2).setText(0, _translate("settings", "Расчет.xlsx"))
        self.treeProjectStruct.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("settings", "При завершении"))
        self.checkBox_openfolder.setText(_translate("settings", "Открывать папку с проектом"))
        self.checkBox_openpayment.setText(_translate("settings", "Открывать расчет"))
        self.groupBox_5.setTitle(_translate("settings", "Общий доступ к настройкам"))
        self.SharedButton.setText(_translate("settings", "..."))
        self.sharedCheckBox.setText(_translate("settings", "Включить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("settings", "Общие"))
        self.btn_save.setText(_translate("settings", "Сохранить"))
