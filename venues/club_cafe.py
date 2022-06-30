from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import ssl
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

from venues.entries import Event

def clubcafe():
    url = "https://www.ticketweb.com/venue/club-cafe-pittsburgh-pa/23219"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    browser.quit()
    results = soup.find_all('li', class_='media theme-mod')
    for result in results:
        listing = Event()
        listing.name = result.find('p', class_='event-name theme-title').text.strip()
        listing.desc = 'n/a'
        listing.date = result.find('p', class_='event-date theme-subTitle').text.strip()
        listing.link = result.find('a', class_='event-title')['href']
        try:
            listing.time = result.find('span', class_='doors-open').text.strip()
        except(AttributeError):
            listing.time = result.find('span', class_='start-time').text.strip()
        return(listing.entry_output)
