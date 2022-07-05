from bs4 import BeautifulSoup as bs
from venue_classes.venue import Venue
from typing import Iterable
from entries import Event
from urllib.request import Request, urlopen
import ssl
import requests

class ClubCafe(Venue):
    @property
    def url(self) -> str:
        return "https://www.ticketweb.com/venue/club-cafe-pittsburgh-pa/23219"

    # def get_response(self):
    #     request = requests.get(self.url)
    #     response = request.text
    #     return request.status_code

    def get_response(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        request = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(request).read()
        soup = bs(page, 'html.parser')
        return soup.find_all('li', class_='media theme-mod')

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            name = listing.find('p',class_="event-name theme-title").text.strip()
            desc = "n/a"
            date = listing.find('p', class_="event-date theme-subTitle").text.strip().split(" ",-1)[1] + " " + listing.find('p', class_="event-date theme-subTitle").text.strip().split(" ",-1)[2]
            link = listing.find('a',class_="media-object img-mask theme-separator-strokes")['href']
            venue = "ClubCafe"
            time = listing.find('p', class_="event-date theme-subTitle").text.strip().split(" ",-1)[6] + " " + listing.find('p', class_="event-date theme-subTitle").text.strip().split(" ",-1)[7]

            yield Event(name, desc, date, time, link, venue)