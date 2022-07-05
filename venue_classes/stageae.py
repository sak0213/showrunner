from bs4 import BeautifulSoup as bs
from venue_classes.venue import Venue
from typing import Iterable
from entries import Event
from urllib.request import Request, urlopen
import ssl

class StageAE(Venue):
    @property
    def url(self) -> str:
        return "https://promowestlive.com/pittsburgh/stage-ae"

    def get_response(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        request = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(request).read()
        soup = bs(page, 'html.parser')
        return soup.find_all('li', class_='card card-horizontal with-box-link')

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            meta = listing.find('div', class_='info')
            name = meta.find("h2").text.strip()
            try:
                desc = meta.find("h3").text.strip()
            except(AttributeError):
                desc = "n/a"
            date = listing.find('time', class_='venue-stage-ae').text.strip()
            link = listing.find('a', class_='box-link')['href']
            venue = "Stage AE"
            time = meta.find('span', class_='doors-time').text.strip()

            yield Event(name, desc, date, time, link, venue)