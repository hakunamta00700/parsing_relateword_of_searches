# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchdlg.ui'
#
# Created: Fri Sep 26 00:06:34 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchDialog(object):
    def setupUi(self, SearchDialog):
        SearchDialog.setObjectName("SearchDialog")
        SearchDialog.resize(1058, 808)
        self.verticalLayout = QtWidgets.QVBoxLayout(SearchDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnDaum = QtWidgets.QPushButton(SearchDialog)
        self.btnDaum.setObjectName("btnDaum")
        self.horizontalLayout_2.addWidget(self.btnDaum)
        self.btnNaver = QtWidgets.QPushButton(SearchDialog)
        self.btnNaver.setObjectName("btnNaver")
        self.horizontalLayout_2.addWidget(self.btnNaver)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.webView = QtWebKitWidgets.QWebView(SearchDialog)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.horizontalLayout.addWidget(self.webView)
        self.listWidget = QtWidgets.QListWidget(SearchDialog)
        self.listWidget.setMinimumSize(QtCore.QSize(256, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(256, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SearchDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SearchDialog)
        self.buttonBox.accepted.connect(SearchDialog.accept)
        self.buttonBox.rejected.connect(SearchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SearchDialog)

    def retranslateUi(self, SearchDialog):
        _translate = QtCore.QCoreApplication.translate
        SearchDialog.setWindowTitle(_translate("SearchDialog", "연관 검색어 추출기"))
        self.btnDaum.setText(_translate("SearchDialog", "다음"))
        self.btnNaver.setText(_translate("SearchDialog", "네이버"))

from PyQt5 import QtWebKitWidgets
