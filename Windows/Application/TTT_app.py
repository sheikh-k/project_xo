import sys
from PyQt6.QtWidgets import QApplication , QMainWindow ,QWidget, QPushButton , QLabel
from PyQt6.QtGui import QIcon ,QFont

Font = QFont('arial',12)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('XO')
        self.setGeometry(100,100,400,300)
        self.setWindowIcon(QIcon(r'Resource\icon.png'))
        
        center = QWidget()
        button = QPushButton('Play',center)
        button.setFont(Font)
        button.clicked.connect(ps1)
        self.setCentralWidget(center)

class Gamewindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('XO')
        self.setGeometry(100,100,400,300)
        self.setWindowIcon(QIcon(r'Resource\icon.png'))
        
        center = QWidget()
        tital = QLabel('Gaming',center)
        tital.setFont(Font)
        self.setCentralWidget(center)

        
def main(): 
    global Window1 , window2 
    app = QApplication(sys.argv)
    Window1 = MainWindow()
    Window1.show()
    
    window2 = Gamewindow()
    
    sys.exit(app.exec())
def ps1():
    Window1.hide()
    window2.show()
    

if __name__ == '__main__':
    main()