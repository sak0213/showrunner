from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import certifi
import ssl

from venues.entries import Event

def mrsmalls():
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://mrsmalls.com/listing/"
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(request).read()
    soup = bs(page, 'html.parser')
    results = soup.find_all('div', class_='cell small-12 event')
    # print(results[:1])
    for result in results:
        listing = Event()
        listing.name = result.find('h4', class_='show-title').text.strip()
        listing.desc = 'n/a'
        listing.date = result.find('div', class_='date-show').text.strip()
        listing.link = result.find('a', class_='event-title')['href']
        try:
            listing.time = result.find('span', class_='doors-open').text.strip()
        except(AttributeError):
            listing.time = result.find('span', class_='start-time').text.strip()
        return(listing.entry_output)
