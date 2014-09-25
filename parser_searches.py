# -*- coding: utf-8 -*-
# 주석은 주석 바로 아래에 있는 줄의 코드를 설명


# python에서 c++를 사용할 수 있게 해주는 모듈임.
import sip 
'''
python에서 Qt를 사용시, 문자열을 다룰 때 Qt의 QString 을 사용하는 것이 아니라  Python 문자열 모듈을 사용하는 것으로 세팅

QVariant 도 마찬가지임
'''
sip.setapi('QString', 2) 
sip.setapi('QVariant', 2)

# sublime-text 에서 콘솔 한글 출력을 위해서
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())  

# 기본적인 PyQt5 import module --- start
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *

# QtDesigner 를 이용하여 pyuic5 를 이용하여 생성한 ~_ui.py 파일의 import
from searchdlg_ui import Ui_SearchDialog

# 각 검색엔진의 url과 연관검색어를 추출하기 위한 태그 Selector
engineInfoDict = {
    "naver": {
        "url": "http://www.naver.com",
        "selector": "[data-acr]"
    },
    "daum": {
        "url": "http://www.daum.net",
        "selector": "[class^=\"idx\"]"
    }
}


# Dialog 클래서의 정의
# QDialog, 와 Ui_SearchDialog - QtDesigner 를 이요하여 만든 거
# 다중 상속 받아서  SearchDialog 를 정의
class SearchDialog(QDialog, Ui_SearchDialog):

    # 생성자 
    # 기본적으로 __init__ 이 파이썬에서 클래스의 생성자임
    # parent라는 변수로 입력을 받을 수 있음.( Qt에서는 각각의 오브젝트들의 부모 오브젝트를 지정할 수 있기 때문에 생성자에서 이렇게 해줘야 함. None을 입력하면 parent가 없고 자신이 최상위)
    def __init__(self, parent=None):
        # 상속 받은 부모의 생성자를 실행하는 구문
        super(SearchDialog, self).__init__(parent)
        # designer로 만든 ui 세팅
        self.setupUi(self)



        # webView에서 page를 파싱하기 위한 page의 따로 변수로 .
        self.currentPage = self.webView.page()

        # 해당 페이지의 컨텐츠 내용이 바뀔 때 마다 시그널을 날리는데 해당 시그널에 대한 슬로을 커넥션 하는 부분
        self.currentPage.contentsChanged.connect(self.onContentsChanged)


        self.currentSearchEngine = None
        self.currentUrl = None
        self.currentSelector = None

        # GUI 메뉴 상단의 버튼 마다 파싱 정보를 세팅하기 위해서 각각 버튼의 클릭 시그널에 대하여 슬롯을 연결함.
        self.btnNaver.clicked.connect(self.onClicked_btnNaver)
        self.btnDaum.clicked.connect(self.onClicked_btnDaum)

    def setCurrentEngineInfo(self, infoDict):
        self.currentUrl = infoDict["url"]
        self.currentSelector = infoDict["selector"]

    def onClicked_btnNaver(self):
        infoDict = engineInfoDict["naver"]
        self.setCurrentEngineInfo(infoDict)
        self.renewCurrentPage()

    def onClicked_btnDaum(self):
        infoDict = engineInfoDict["daum"]
        self.setCurrentEngineInfo(infoDict)
        self.renewCurrentPage()

    def onContentsChanged(self):
        # print("onContentsChanged!!!!!!")
        self.listWidget.clear()
        doc = self.__getDoc()
        el_list = doc.findAll(self.currentSelector)
        for el in el_list:
            self.listWidget.addItem(QListWidgetItem(el.toPlainText().strip()))

    def renewCurrentPage(self):
        self.webView.load(QUrl(self.currentUrl))

    def __getDoc(self):
        return self.currentPage.mainFrame().documentElement()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = SearchDialog()
    dlg.show()
    sys.exit(app.exec_())
