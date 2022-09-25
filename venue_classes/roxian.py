from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import ssl
from venue_classes.venue import Venue
from typing import Iterable
from entries import Event
from datetime import datetime

class Roxian(Venue):
    @property
    def url(self) -> str:
        return "https://www.livenation.com/venue/KovZ917Ax13/roxian-theatre-events"

    def get_response(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        request = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(request).read()
        soup = bs(page, 'html.parser')
        return soup.find_all('li', class_='listing__item')

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            try:
                name = listing.find('h3').text.strip()
                desc = listing.find('h4').text.strip()
                try:
                    source_date = listing.find('time')['datetime'].split("T",1)[0]
                    date = datetime.strptime(source_date, '%Y-%m-%d').date()
                    date = str(date)
                except:
                    date = listing.find('time')['datetime'].split("T",1)[0]
                link = listing.find('a', class_='listing__item__link')['href']
                venue = "Roxian"
                time = listing.find('time')['datetime'].split("T",1)[1]
                yield Event(name, desc, date, time, link, venue)
            except(TypeError):
                pass
