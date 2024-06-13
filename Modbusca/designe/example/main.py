from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
    
        self.setWindowTitle('ModbusView')
        self.setGeometry(300,250,400,200)

        self.new_text  = QtWidgets.QLabel(self)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(100,100)
        self.btn.setText('Подключиться')
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)
       
    def add_label(self):
       self.new_text.setText('Надпись')
       self.new_text.move(100,50)
       self.new_text.adjustSize()





def application():
    app = QApplication(sys.argv)
    window = Window()


    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()