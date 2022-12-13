import requests
from bs4 import BeautifulSoup
import time
   
def get_2_price(self, model):
    """Returns the second hand price of the specified vehicle model.
    param model: car's model"""
    try:
        self.model_name = model.replace(" ", "+")
        self.url2 = "https://www.arabam.com/ikinci-el?membertype=Sahibinden&searchText=" + self.model_name + "&sort=priceTl.asc"
        self.r = requests.get(self.url2, headers = {'User-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'})
        self.soup2 = BeautifulSoup(self.r.content, features="html.parser")
        self.pricess_2 = []
        self.prices_2 = self.soup2.find_all("a", {"class":"listing-price"})
        
        for self.price in self.prices_2:
            self.pricess_2.append(self.price.text)
        
        return self.pricess_2[0]
    except:
        return " Fiyat Bulunamadı."
        
def get_cars(self,brand):
    """Returns the model names of models of the specified brand.
    param brand: car's model"""
    self.url = "https://www.sifiraracal.com/" + brand + "-modelleri"
    self.r = requests.get(self.url)
    self.soup = BeautifulSoup(self.r.content, features="html.parser")
    self.cars = self.soup.find_all("h2")
    self.brandcars = []
    for self.car in self.cars:
        self.brandcars.append(self.car.text.replace("\n", ""))
    
    return self.brandcars
    
def get_pictures(self, brand):
    """Returns the pictures of models of the specified brand.
    param brand: car's model"""
    self.url = "https://www.sifiraracal.com/" + brand + "-modelleri"
    self.r = requests.get(self.url)
    self.soup = BeautifulSoup(self.r.content, features="html.parser")
    self.picture = self.soup.find("div", {"class": "fiyatlars"}, "strong")
    
def get_prices(self,brand,index):
    """Returns the prices of models of the specified brand.
    param brand: car's model"""
    self.url = "https://www.sifiraracal.com/" + brand + "-modelleri"
    self.r = requests.get(self.url)
    self.soup = BeautifulSoup(self.r.content, features="html.parser")
    
    self.prices = self.soup.find_all("div", {"class": "fiyatlars"}, "strong")
    self.allprices = []
    for self.price in self.prices:
        self.allprices.append(self.price.text.replace("\n", ""))
    
    return self.allprices[index-1]

def get_car_link(self, brand):
    """Returns the site links of the models of the specified brand.
    param brand: car's model"""
    try:
        self.model_name = brand.replace(" ", "+")
        self.url = "https://www.arabam.com/ikinci-el?membertype=Sahibinden&searchText=" + self.model_name + "&sort=priceTl.asc"
        self.r = requests.get(self.url, headers = {'User-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'})
        self.soup = BeautifulSoup(self.r.content, features="html.parser")
        self.link = self.soup.find("a", {"class": "listing-text-new word-break"})
        
        return self.link["href"]
    except:
        return ""
