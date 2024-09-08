import requests as rs
from bs4 import BeautifulSoup as bs

    
    
class Calculator:
    def __init__(self, url):
        self.url = url
        self.head = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
        self.res = rs.get(self.url, self.head)
        self.soup = bs(self.res.text, 'html.parser')
    
    def get_data(self):
        self.res = rs.get(self.url, self.head)
        ax = 
        
    def calculate_ratio(num1: int, num2: int):
        if num1 > num2:
            if num2 == 0:
                return num1
            else:
                rest = num1%num2
                return Calculator.calculate_ratio(num2,rest)
        elif num2 > num1:
            if num1 == 0:
                return num2
            else:
                rest = num2%num1
                return Calculator.calculate_ratio(num2,rest)