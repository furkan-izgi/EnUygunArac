import requests
from bs4 import BeautifulSoup
import time
   
def get_2_price(self, model):
    try:
        self.model_name = model.replace(" ", "+")
        self.url2 = "https://www.arabam.com/ikinci-el?membertype=Sahibinden&searchText=" + self.model_name + "&sort=priceTl.asc"
        self.r = requests.get(self.url2, headers = {'User-agent': 'your bot 0.1'})
        self.soup2 = BeautifulSoup(self.r.content, features="html.parser")
        self.pricess_2 = []
        self.prices_2 = self.soup2.find_all("a", {"class":"listing-price"})
        
        for self.price in self.prices_2:
            self.pricess_2.append(self.price.text)
        
        return self.pricess_2[0]
    except:
        return " Fiyat Bulunamadı."
        
def get_cars(self,model):
    self.url = "https://www.sifiraracal.com/" + model + "-modelleri"
    self.r = requests.get(self.url)
    self.soup = BeautifulSoup(self.r.content, features="html.parser")
    self.cars = self.soup.find_all("h2")
    self.carr = []
    for self.car in self.cars:
        self.carr.append(self.car.text.replace("\n", ""))
    
    return self.carr
    
def get_pictures(self, model):
    self.url = "https://www.sifiraracal.com/" + model + "-modelleri"
    self.r = requests.get(self.url)
    self.soup = BeautifulSoup(self.r.content, features="html.parser")
    self.picture = self.soup.find("div", {"class": "fiyatlars"}, "strong")
    
def get_prices(self,model,index):
    self.url = "https://www.sifiraracal.com/" + model + "-modelleri"
    self.r = requests.get(self.url)
    self.soup = BeautifulSoup(self.r.content, features="html.parser")
    
    self.prices = self.soup.find_all("div", {"class": "fiyatlars"}, "strong")
    self.pricess = []
    for self.price in self.prices:
        self.pricess.append(self.price.text.replace("\n", ""))
    
    return self.pricess[index-1]

def get_car_link(self, model):
    try:
        self.model_name = model.replace(" ", "+")
        self.url2 = "https://www.arabam.com/ikinci-el?membertype=Sahibinden&searchText=" + self.model_name + "&sort=priceTl.asc"
        self.r = requests.get(self.url2, headers = {'User-agent': 'your bot 0.1'})
        self.soup2 = BeautifulSoup(self.r.content, features="html.parser")
        self.link = self.soup2.find("a", {"class": "listing-text-new word-break"})
        
        return self.link["href"]
    except:
        return ""
