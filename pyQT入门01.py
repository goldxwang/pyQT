#-*- coding:utf-8 -*-
#1. 一个简单的框架：
import sys
from PyQt5.QtWidgets import QApplication, QWidget
#导入必要的相关库

if __name__ == '__main__':
    w = QWidget()
    w.show()

    app = QApplication(sys.argv)
    sys.exit(app.exec_())