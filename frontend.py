from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QAction, QApplication, QComboBox, QLabel, QMainWindow, QMessageBox, QPushButton
import sys
import frontend_funcs as ff
import backend
import webbrowser
      
class Window(QMainWindow):
        
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    
    def whiteTheme(self):
        self.variables  = [self.lbl_marka_info,self.lbl_model_info,self.lbl_2_fiyat,self.lbl_title,self.lbl_marka,self.lbl_model,self.marka_btn,self.model_btn,self.lbl_sifir_fiyat,self.combobox_marka,self.combobox_model,self.about]
               
        self.setStyleSheet("background-color: #dee3e3;")
        
        for variable in self.variables:#Bütün labellar, butonlar, comboboxların text colorları değiştirildi!
            variable.setStyleSheet("color: black;")
            
        self.menubar.setStyleSheet("background-color:#dee3e3; color:black;")
   
    def grayTheme(self):       
        self.variables  = [self.lbl_marka_info,self.lbl_model_info,self.lbl_2_fiyat,self.lbl_title,self.lbl_marka,self.lbl_model,self.marka_btn,self.model_btn,self.lbl_sifir_fiyat,self.combobox_marka,self.combobox_model,self.about]
        
        self.setStyleSheet("background-color: #424751;")
        
        for variable in self.variables:
            variable.setStyleSheet("color:white;")
            
        self.menubar.setStyleSheet("background-color: #424751; color:white;")
                
    def initUI(self):
        self.setGeometry(100, 100, 610, 400)
        self.setWindowTitle("En Uygun Araç")
        self.setWindowIcon(QIcon("assets\\app.svg"))
        #################################################################################################################
        self.marka_dicts= {"Audi":"audi", "Bmw":"bmw", "Citroen":"citroen", "Dacia":"dacia","Fiat":"fiat", "Ford":"ford","Honda":"honda","Hyundai":"hyundai",
                           "Isuzu":"isuzu", "Jaguar":"jaguar", "Jeep":"jeep","Kia":"kia","Lada":"lada", "Land Rover":"land-rover","Lexus":"lexus", 
                           "Maserati":"maserati", "Mazda":"mazda","Mercedes":"mercedes","Mg":"mg", "Mini":"mini","Mitsubishi":"mitsubishi","Nissan":"nissan",
                           "Opel":"opel", "Peugeot":"peugeot","Porsche":"porsche","Renault":"renault", "Seat":"seat","Skoda":"skoda","Smart":"smart", 
                           "Ssangyong":"ssangyong", "Subaru":"subaru","Suzuki":"suzuki", "Toyota":"toyota", "Volkswagen":"volkswagen", "Volvo":"volvo"}
        #################################################################################################################
        self.logo = QPixmap("assets/app.svg").scaled(20, 20, QtCore.Qt.KeepAspectRatio)
        self.lbl_logo = QLabel(self)
        self.lbl_logo.setPixmap(self.logo)
        self.lbl_logo.move(240, 15)
        
        self.lbl_title = QLabel("En Uygun Araç", self)
        self.lbl_title.move(265, 15)
        
        self.lbl_marka = QLabel("Marka", self)
        self.lbl_marka.move(130, 50)
        self.lbl_marka.setFixedWidth(400)
        
        self.lbl_model = QLabel("Model",self)
        self.lbl_model.move(430, 50)
        self.lbl_model.setFixedWidth(400)
        
        self.marka_btn  = QPushButton("Marka Seç",self)
        self.marka_btn.move(50, 140)
        self.marka_btn.clicked.connect(lambda marka_name: ff.Funcs.getMarka(self, marka_name))
        
        self.model_btn  = QPushButton("Model Seç",self)
        self.model_btn.move(350, 140)
        self.model_btn.setEnabled(False)
        self.model_btn.clicked.connect(lambda model_name: ff.Funcs.getModel(self, model_name))
        
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
        self.pic_lbl.move(280, 180)
        self.pic_lbl.resize(350,200)
        
        self.menubar = self.menuBar()
        
        self.settings = self.menubar.addMenu("&Ayarlar")
        self.pic_settings = self.settings.addMenu("&Görüntü")
        self.menubar.addSeparator()
        self.theme = self.settings.addMenu("&Temalar")
        self.about = self.menubar.addMenu("&Hakkında")
        
        self.toolbar = QtWidgets.QToolBar("Example")
        self.toolbar.setMovable(False)
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolbar)
        
        self.pic_on = QAction(QIcon("assets/icons/pic_on.png"), "Resimleri &Aç", self)
        self.pic_on.setShortcut("Ctrl+O")
        self.pic_on.triggered.connect(lambda: ff.Funcs.picOn(self))
        
        self.pic_off = QAction(QIcon("assets/icons/pic_off.png"), "Resimleri &Kapat", self)
        self.pic_off.setShortcut("Ctrl+C")
        self.pic_off.triggered.connect(lambda: ff.Funcs.picOff(self))
        
        self.gray_theme = QAction(QIcon("assets/icons/gray.png"), "&Gri Tema", self)
        self.gray_theme.triggered.connect(lambda: Window.grayTheme(self))
        
        self.white_theme = QAction(QIcon("assets/icons/white.png"), "&Beyaz Tema", self)
        self.white_theme.triggered.connect(lambda: Window.whiteTheme(self))
        
        self.github = QAction(QIcon("assets/icons/github.png"), "&Github", self)
        self.github.triggered.connect(lambda: webbrowser.open_new('https://github.com/Furkan-izgi'))
        
        self.linkedin = QAction(QIcon("assets/icons/linkedin.png"), "&Linkedin", self)
        self.linkedin.triggered.connect(lambda: webbrowser.open_new('https://www.linkedin.com/in/furkan-izgi/'))
        #########################################################################################################
        self.about.addAction(self.github)
        self.about.addAction(self.linkedin)
        
        self.pic_settings.addAction(self.pic_on)
        self.pic_settings.addAction(self.pic_off)
        
        self.toolbar.addAction("").setEnabled(False)#Toolbardaki fonksiyonların arasına boşluk eklemek için kullanıldı.
        self.toolbar.addAction("").setEnabled(False)
        self.toolbar.addAction("").setEnabled(False)
        
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.pic_on)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.pic_off)
        self.toolbar.addSeparator()
        
        self.toolbar.addAction("").setEnabled(False)
        self.toolbar.addAction("").setEnabled(False)
        
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.gray_theme)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.white_theme)
        self.toolbar.addSeparator()
        
        self.toolbar.addAction("").setEnabled(False)
        self.toolbar.addAction("").setEnabled(False)
        
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.github)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.linkedin)
        self.toolbar.addSeparator()
        
        self.theme.addAction(self.white_theme)
        self.theme.addAction(self.gray_theme)
        
        
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
    win.grayTheme()
    sys.exit(app.exec())
