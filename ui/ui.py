from kiwoom.kiwoom import *
import sys
from PyQt5.QtWidgets import *

class Ui_class():
    def __init__(self):
        print("UI 클래스입니다")

        self.app = QApplication(sys.argv)

        self.kiwoom = Kiwoom()
        # Process finished with exit code -1073740777 (0xC0000417)
        # 변수를 하나 만든다
        self.app.exec_()  ###종료가 되지 않는다.