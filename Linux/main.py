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
        self.progressBar.setValue(10)
        os.system("sudo apt update")
        self.progressBar.setValue(30)
        os.system("sudo apt upgrade -y")
        self.progressBar.setValue(40)
        os.system("sudo apt autoremove -y")
        self.progressBar.setValue(50)
        os.system("sudo apt autoclean -y")
        self.progressBar.setValue(60)
        os.system("sudo history -c")
        self.progressBar.setValue(70)
        os.system("sudo swapoff -a")
        self.progressBar.setValue(80)
        os.system("sudo swapon -a")
        self.progressBar.setValue(90)
        os.system("sudo rm -rf /home/$USER/.cache/*")
        self.progressBar.setValue(100)
        self.progressBar.setValue(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())