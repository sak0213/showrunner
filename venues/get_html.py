from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import requests
from selenium import webdriver
import ssl
import time

def get_html(url):
    req = requests.get(url)
    if req.status_code == 403:
        ssl._create_default_https_context = ssl._create_unverified_context
        request = Request(url, headers={'User-Agent': 'Mozilla'})
        page = urlopen(request).read()
        print('solved 403')
        return page
    elif req.status_code == 200:
        print('solved 200')
        return req.text
    elif req.status_code == 101:
        driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
        print(url)
        driver.get(url)
        page = driver.page_source
        print('solved 101')
        return page

    print(req.status_code)



urls = ['https://mrsmalls.com/listing/', 'https://www.ticketweb.com/venue/club-cafe-pittsburgh-pa/23219', "https://www.spiritpgh.com/events?view=calendar&month=06-2022"]

for url in urls:
    get_html(url)