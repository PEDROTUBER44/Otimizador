from PyQt5 import uic, QtWidgets
from app import Ui_Dialog
import os 
import sys

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)
        self.pushButton.clicked.connect(self.logs)
        self.progressBar.setRange(0, 100)
        self.show()
    
    def logs(self):
    	self.progressBar.setValue(0)
        self.progressBar.setValue(20)
        os.system(r"rd /S /Q c:\$Recycle.bin")
        self.progressBar.setValue(40)
        os.system(r"del /q C:\Windows\Prefetch\*")
        self.progressBar.setValue(60)
        os.system(r"del /q C:\Users\%username%\AppData\Local\Temp\*")
        self.progressBar.setValue(70)
        os.system(r"del /q C:\Windows\Temp\*")
        self.progressBar.setValue(80)
        os.system(r"del /q C:\Users\%username%\AppData\Local\Google\Chrome\User Data\Default\Cache\*")
        self.progressBar.setValue(100)
        self.progressBar.setValue(0)
        exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())