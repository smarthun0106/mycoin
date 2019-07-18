''' PyQt - 윈도우꾸미기'''
# import sys
# from PyQt5.QtWidgets import *
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # 윈도우 창 크기 조절
#         self.setGeometry(1000, 600, 300, 200)
#         # 윈도우 타이틀 변경
#         self.setWindowTitle("PyQt")
#
#         # 버튼생성 및 연결
#         btn1 = QPushButton('버튼1', self) # 버튼생성
#         btn1.move(20, 20) # 버튼 위치
#         btn1.clicked.connect(self.btn1_clicked) # 버튼 연결
#
#     # 버튼 이벤트
#     def btn1_clicked(self):
#         print("버튼클릭")
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
#
# app.exec_()

''' PyQt - desiner로 꾸민거 ui로 가져오기 '''
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# import pykorbit
#
# form_class = uic.loadUiType("button.ui")[0]
#
# class MyWindow(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.pushButton.clicked.connect(self.btn_clicked)
#
#     def btn_clicked(self):
#         price = pykorbit.get_current_price("BTC")
#         self.lineEdit.setText(str(price))
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()

''' QTimer 사용 '''
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import QTimer, QTime
# from PyQt5 import uic
# import pykorbit
# form_class = uic.loadUiType("button.ui")[0]
#
# class MyWindow(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.pushButton.clicked.connect(self.btn_clicked)
#         self.timer = QTimer(self)
#         self.timer.start(1000) # interval 설정
#         self.timer.timeout.connect(self.btn_clicked) # timeout1 함수 연결
#
#     def btn_clicked(self):
#         price = pybithumb.get_current_price("BTC")
#         self.lineEdit.setText(str(price))
#         cur_time = QTime.currentTime()
#         str_time = cur_time.toString("hh:mm:ss")
#         self.statusBar().showMessage(str_time)
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()
