from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QAction, QApplication, QComboBox, QLabel, QMainWindow, QMessageBox, QPushButton
import backend

class Funcs(QMainWindow):
   
    def modelsName(self):
        self.lbl_model_info.setText("Model             : ")
        self.combobox_model.clear()
        self.combobox_model.addItem("Model Seçiniz...")
        self.combobox_model.addItems(backend.get_cars(self,self.brand_dicts[self.combobox_brand.currentText()]))
        self.combobox_model.setCurrentText("Model Seçiniz...")   
        
    def getPicture(self):
        self.model_index = self.combobox_model.currentIndex()
        self.pic = QPixmap("assets\\" + self.brand_dicts[self.combobox_brand.currentText()] + "\\"+ str(self.model_index) +".webp").scaled(310, 310, QtCore.Qt.KeepAspectRatio)
             
    def getModel(self,model_name):
        model_name = self.combobox_model.currentText()
        
        if model_name == "Model Seçiniz...":
            QMessageBox.warning(self,"Hata","Lütfen bir model seçiniz!",QMessageBox.Ok)
            
        else:
            self.model_index = self.combobox_model.currentIndex()
            self.link = backend.get_car_link(self, model_name)
            self.lbl_model_info.setText("Model             : " + model_name)
            self.lbl_price.setText("Sıfır Fiyatı       :" + backend.get_prices(self, self.brand_dicts[self.combobox_brand.currentText()], self.model_index))
            self.lbl_2_price.setText("En Ucuz 2.El Fiyatı  :" + backend.get_2_price(self, model_name))
            if self.link == "":
                self.car_link.setText('')
            else:
                self.car_link.setText('<a href = https://www.arabam.com' + self.link + '>Link</a>')
            Funcs.getPicture(self)
            self.pic_lbl.setPixmap(self.pic)
            
    def getBrand(self,marka_name):
        marka_name = self.combobox_brand.currentText()
        if marka_name == "Marka Seçiniz...":
            QMessageBox.warning(self,"Hata","Lütfen bir marka seçiniz!",QMessageBox.Ok)
        else:
            self.lbl_brand_info.setText("Marka             : " + marka_name)
            self.lbl_model_info.setText("Model             : ")
            self.lbl_price.setText("Sıfır Fiyatı       :")
            self.lbl_2_price.setText("En Ucuz 2.El Fiyatı  :")
            Funcs.modelsName(self)
            self.model_btn.setEnabled(True)
            
    def picOn(self):
        self.pic_lbl.resize(350,200)
    
    def picOff(self):
        self.pic_lbl.resize(0,0)
