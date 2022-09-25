from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import ssl
from venue_classes.venue import Venue
from typing import Iterable
from entries import Event
from datetime import datetime

class MrSmalls(Venue):
    @property
    def url(self) -> str:
        return "https://mrsmalls.com/listing/"

    def get_response(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        request = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(request).read()
        soup = bs(page, 'html.parser')
        return soup.find_all('div', class_='cell small-12 event')

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            name = listing.find('h4', class_='show-title').text.strip()
            desc = 'n/a'
            try:
                date_pulled = listing.find('div', class_='date-show').text.strip()
                date = datetime.strptime(date_pulled,'%A, %B %d, %Y').date()
                date = str(date)
            except:
                date = listing.find('div', class_='date-show').text.strip()
            link = listing.find('a', class_='event-title')['href']
            venue = "Mr. Smalls"
            try:
                time = listing.find('span', class_='doors-open').text.strip()
            except(AttributeError):
                time = listing.find('span', class_='start-time').text.strip()
            yield Event(name, desc, date, time, link, venue)