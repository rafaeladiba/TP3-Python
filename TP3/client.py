import webbrowser
import requests
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys

class Main():
    def query(self, hostname):
        url="http://%s" %(hostname)
        r=requests.get(url)
        if r.status_code==requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your IP to localizate:", self)
        self.text = QLineEdit(self)
        self.label1.move(10,10)
        self.text.move(10, 30)
        self.label2 = QLabel("Enter your API KEY:", self)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 85)
        self.label2.move(10,65)
        self.label3 = QLabel("Enter a hostname IP:", self)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 140)
        self.label3.move(10,120)

        
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 170)
        self.button = QPushButton("Send", self)
        self.button.move(10, 190)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        ip = self.text.text()
        key = self.text2.text()
        hostname=self.text3.text()
      

        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,ip,key)
            #res=self.__query2( "%s" %(res["latitude"]),"%s" %(res["longitude"]))
            if res:
                self.label2.setText("latitude%s" % (res["Latitude"]))
                self.label2.adjustSize()
                self.label3.setText("longitude%s" % (res["Longitude"]))
                self.label3.adjustSize()
                self.show()
                url = "https://www.openstreetmap.org/?mlat=%s&mlon=%s" %((res["Latitude"]),res["Longitude"])
                print(url)
                webbrowser.open(url)
                

    def __query(self, hostname,ip,key):
        url = "http://%s/ip/%s?key=%s" % (hostname,ip,key)
        print(url)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()
            #webbrowser.open(r)

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()

"""if __name__ == "__main__":

    main = Main()
    hostname = "127.0.0.1:8000"
    res = main.query(hostname)
    if res:
        print(res)"""