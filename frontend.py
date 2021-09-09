from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QAction, QApplication, QComboBox, QLabel, QMainWindow, QMessageBox, QPushButton
import sys
import backend
import webbrowser

class WinTable(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hakkında")
        self.setGeometry(100, 100, 400, 400) 
        
class Window(QMainWindow):
        
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    
    def aboutWindow(self):
        self.winTable = WinTable()
        self.winTable.show()
    
    def modelsName(self):
        self.lbl_model_info.setText("Model             : ")
        self.combobox_model.clear()
        self.combobox_model.addItem("Model Seçiniz...")
        self.combobox_model.addItems(backend.get_cars(self,self.marka_dicts[self.combobox_marka.currentText()]))
        self.combobox_model.setCurrentText("Model Seçiniz...")   
        
    def getPicture(self):
        self.model_index = self.combobox_model.currentIndex()
        self.pic = QPixmap("assets\\" + self.marka_dicts[self.combobox_marka.currentText()] + "\\"+ str(self.model_index) +".png").scaled(360, 360, QtCore.Qt.KeepAspectRatio)
             
    def getModel(self,model_name):
        model_name = self.combobox_model.currentText()
        
        if model_name == "Model Seçiniz...":
            QMessageBox.warning(self,"Hata","Lütfen bir model seçiniz!",QMessageBox.Ok)
            
        else:
            self.model_index = self.combobox_model.currentIndex()
            self.link = backend.get_car_link(self, model_name)
            self.lbl_model_info.setText("Model             : " + model_name)
            self.lbl_sifir_fiyat.setText("Sıfır Fiyatı       :" + backend.get_prices(self, self.marka_dicts[self.combobox_marka.currentText()], self.model_index))
            self.lbl_2_fiyat.setText("En Ucuz 2.El Fiyatı  :" + backend.get_2_price(self, model_name))
            if self.link == "":
                self.car_link.setText('')
            else:
                self.car_link.setText('<a href = https://www.arabam.com' + self.link + '>Link</a>')
            Window.getPicture(self)
            self.pic_lbl.setPixmap(self.pic)
            
            
    def getMarka(self,marka_name):
        marka_name = self.combobox_marka.currentText()
        if marka_name == "Marka Seçiniz...":
            QMessageBox.warning(self,"Hata","Lütfen bir marka seçiniz!",QMessageBox.Ok)
        else:
            self.lbl_marka_info.setText("Marka             : " + marka_name)
            self.lbl_model_info.setText("Model             : ")
            self.lbl_sifir_fiyat.setText("Sıfır Fiyatı       :")
            self.lbl_2_fiyat.setText("En Ucuz 2.El Fiyatı  :")
            Window.modelsName(self)
            self.model_btn.setEnabled(True)
            
    def picOn(self):
        self.pic_lbl.resize(330,200)
    
    def picOff(self):
        self.pic_lbl.resize(0,0)
    
    def initUI(self):
        self.setGeometry(100, 100, 600, 370)
        self.setWindowTitle("En Uygun Araç")
        self.setWindowIcon(QIcon("assets\\app.svg"))
        self.setStyleSheet("background-color: gray;")
        #################################################################################################################
        self.marka_dicts= {"Audi":"audi", "Bmw":"bmw", "Citroen":"citroen", "Dacia":"dacia","Fiat":"fiat", "Ford":"ford","Honda":"honda","Hyundai":"hyundai",
                           "Isuzu":"isuzu", "Jaguar":"jaguar", "Jeep":"jeep","Kia":"kia","Lada":"lada", "Land Rover":"land-rover","Lexus":"lexus", 
                           "Maserati":"maserati", "Mazda":"mazda","Mercedes":"mercedes","Mg":"mg", "Mini":"mini","Mitsubishi":"mitsubishi","Nissan":"nissan",
                           "Opel":"opel", "Peugeot":"peugeot","Porsche":"porsche","Renault":"renault", "Seat":"seat","Skoda":"skoda","Smart":"smart", 
                           "Ssangyong":"ssangyong", "Subaru":"subaru","Suzuki":"suzuki", "Toyota":"toyota", "Volkswagen":"volkswagen", "Volvo":"volvo"}
        #################################################################################################################
        self.lbl_title = QLabel("En Uygun Araç", self)
        self.lbl_title.move(260, 10)
        
        self.lbl_marka = QLabel("Marka", self)
        self.lbl_marka.move(130, 50)
        self.lbl_marka.setFixedWidth(400)
        
        self.lbl_model = QLabel("Model",self)
        self.lbl_model.move(430, 50)
        self.lbl_model.setFixedWidth(400)
        
        self.marka_btn  = QPushButton("Marka Seç",self)
        self.marka_btn.move(50, 140)
        self.marka_btn.clicked.connect(lambda marka_name: Window.getMarka(self, marka_name))
        
        self.model_btn  = QPushButton("Model Seç",self)
        self.model_btn.move(350, 140)
        self.model_btn.setEnabled(False)
        self.model_btn.clicked.connect(lambda model_name: Window.getModel(self, model_name))
        
        self.lbl_marka_info = QLabel("Marka             :", self)
        self.lbl_marka_info.move(50, 200)
        self.lbl_marka_info.setFixedWidth(400)
        
        self.lbl_model_info = QLabel("Model             :", self)
        self.lbl_model_info.move(50, 230)
        self.lbl_model_info.setFixedWidth(400)
        
        self.lbl_sifir_fiyat = QLabel("Sıfır Fiyatı       :", self)
        self.lbl_sifir_fiyat.move(50, 260)
        self.lbl_sifir_fiyat.setFixedWidth(400)
        
        self.lbl_2_fiyat = QLabel("En Ucuz 2.El Fiyatı  :", self)
        self.lbl_2_fiyat.move(50, 290)
        self.lbl_2_fiyat.setFixedWidth(400)
        
        self.car_link = QLabel("", self)
        self.car_link.move(50, 320)
        self.car_link.setFixedWidth(400)
        self.car_link.setOpenExternalLinks(True)
        
        self.pic_lbl = QLabel(self)
        self.pic_lbl.move(270, 180)
        self.pic_lbl.resize(330,200)
        
        self.menubar = self.menuBar()
        
        self.settings = self.menubar.addMenu("&Ayarlar")
        self.pic_on = QAction("Resimleri &Aç",self)
        self.pic_on.setShortcut("Ctrl+O")
        self.pic_on.setToolTip("Araba resimlerini açar.")
        self.pic_on.triggered.connect(lambda: Window.picOn(self))
        
        self.pic_off = QAction("Resimleri &Kapat",self)
        self.pic_off.setShortcut("Ctrl+C")
        self.pic_on.setToolTip("Araba resimlerini kapatır.")
        self.pic_off.triggered.connect(lambda: Window.picOff(self))
        
        self.settings.addAction(self.pic_on)
        self.settings.addAction(self.pic_off)
        
        self.about = self.menubar.addMenu("&Hakkında")
        
        self.github = QAction("&Github", self)
        self.github.setShortcut("Ctrl+G")
        self.github.triggered.connect(lambda: webbrowser.open_new('https://github.com/Furkan-izgi'))
        
        self.linkedin = QAction("&Linkedin", self)
        self.linkedin.setShortcut("Ctrl+L")
        self.linkedin.triggered.connect(lambda: webbrowser.open_new('https://www.linkedin.com/in/furkan-izgi/'))
        
        self.about.addAction(self.github)
        self.about.addAction(self.linkedin)
        
        ########################################################################
        self.combobox_marka = QComboBox(self)
        self.combobox_marka.move(50, 90)
        self.combobox_marka.setFixedWidth(200)
        self.combobox_marka.addItem("Marka Seçiniz...")
        self.combobox_marka.addItems(self.key for self.key in self.marka_dicts.keys())
        self.combobox_marka.setCurrentText("Marka Seçiniz...")
        self.combobox_model = QComboBox(self)
        self.combobox_model.move(350, 90)
        self.combobox_model.setFixedWidth(200)
        ########################################################################
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec())