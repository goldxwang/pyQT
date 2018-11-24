#-*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        # 这里假设前面已经声明继承了QWidget的类
        #self.resize(width, length)
        self.resize(500, 200)
        self.move(50, 60)  # 左上角为(0,0)点
        self.setGeometry(50, 60, 600, 300)
        self.setWindowTitle('window_title')

    def initUI(self):
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())