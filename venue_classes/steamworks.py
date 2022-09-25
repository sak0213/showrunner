from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import ssl
from venue_classes.venue import Venue
from typing import Iterable
from entries import Event
import re
from datetime import datetime

class Steamworks(Venue):
    @property
    def url(self) -> str:
        return "https://steamworkscreative.com/events/"

    def get_response(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        request = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(request).read()
        soup = bs(page, 'html.parser')
        return soup.find_all('div', id=re.compile('^post-'))

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            name = listing.find('a', class_="tribe-event-url").text.strip()
            try:
                desc = listing.find('div', class_="tribe-events-list-event-description tribe-events-content description entry-summary").text.strip()
            except:
                desc = "n/a"
            try:
                source_date = listing.find('span', class_="tribe-event-date-start").text.strip().split("@",1)[0] + ', 2022'
                date = datetime.strptime(source_date, '%B %d , %Y').date()
                date = str(date)
            except(ValueError):
                source_date = listing.find('span', class_="tribe-event-date-start").text.strip().split("@", 1)[0] + ', 2022'
                date = datetime.strptime(source_date, '%B %d, %Y').date()
                date = str(date)
            except:
                date = listing.find('span', class_="tribe-event-date-start").text.strip().split("@",1)[0]
            link = listing.find('a', class_="tribe-event-url")['href']
            venue = "Steamworks"
            try:
                time = listing.find('span', class_="tribe-event-date-start").text.strip().split("@",1)[1]
            except(IndexError):
                time = "n/a"
            yield Event(name, desc, date, time, link, venue)