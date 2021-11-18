import time
import requests
from bs4 import BeautifulSoup


def get_char_info(name):
    url = 'https://www.mudecay.ru/?character=' + str(name)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    result = soup.find('center', class_= 'resetchar')

    arr = {
        'lvlchar' : soup.find('center', class_= 'lvlchar').text, 
        'racechar' : soup.find('center', class_= 'racechar').text, 
        'namechar' : soup.find('center', class_= 'namechar').text, 
        'resetchar' : soup.find('center', class_= 'resetchar').text if result else "0", 
        'grchar' : soup.find('center', class_= 'grchar').text if result else "0", 
        'lastenterchar' : soup.find('center', class_= 'lastenterchar').text
    }

    return arr