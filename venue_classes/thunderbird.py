from bs4 import BeautifulSoup as bs
from venue_classes.venue import Venue
from typing import Iterable
from entries import Event
from urllib.request import Request, urlopen
import ssl
from datetime import datetime

class Thunderbird(Venue):
    @property
    def url(self) -> str:
        return "https://thunderbirdmusichall.com/"

    def get_response(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        request = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(request).read()
        soup = bs(page, 'html.parser')
        return soup.find_all('div', class_='col-12 col-sm-6 col-lg-4 eventMainWrapper pb-4 d-flex')

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            name = listing.find('a', class_='url')['title']
            desc = 'n/a'
            try:
                source_date = listing.find('div', class_='mb-0 eventMonth singleEventDate text-uppercase').text.strip() + ', 2022'
                date = datetime.strptime(source_date.replace("Sept", "Sep"), '%a, %b %d, %Y').date()
                date = str(date)
            except:
                date = listing.find('div', class_='mb-0 eventMonth singleEventDate text-uppercase').text.strip()
            link = listing.find('a', class_='url')['href']
            venue = "Thunderbird"
            time = listing.find('i', class_='fa fa-clock-o').text.strip()

            yield Event(name, desc, date, time, link, venue)