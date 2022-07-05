from bs4 import BeautifulSoup as bs
from venue_classes.venue import Venue
from typing import Iterable
from entries import Event
from urllib.request import Request, urlopen
import ssl
import re

class CraftHousePGH(Venue):
    @property
    def url(self) -> str:
        return "https://crafthousepgh.com/events-shows/"

    def get_response(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        request = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(request).read()
        soup = bs(page, 'html.parser')
        return soup.find_all('div', class_=re.compile('^pp-content-post pp-content-grid-post'))

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            name = listing.find('span', class_='pp-content-grid-title pp-post-title').text.strip().split("∙", 1)[0]
            desc = 'n/a'
            date = listing.find('span', class_='pp-content-grid-title pp-post-title').text.strip().split("∙", 1)[1]
            link = listing.find('a', class_='pp-post-link')['href']
            venue = "Crafthouse"
            time = 'n/a'

            yield Event(name, desc, date, time, link, venue)