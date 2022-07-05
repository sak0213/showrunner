from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import ssl
from venue_classes.venue import Venue
from typing import Iterable
from entries import Event

class Cattivo(Venue):
    @property
    def url(self) -> str:
        return "https://cattivopgh.com/events"

    def get_response(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        request = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(request).read()
        soup = bs(page, 'html.parser')
        return soup.find_all('div', class_="x-el x-el-div x-el c1-1 c1-2 c1-6x c1-1e c1-b c1-c c1-6y c1-6z c1-d c1-e c1-f c1-g c1-1 c1-2 c1-15 c1-6d c1-6e c1-6f c1-16 c1-6g c1-6h c1-6i c1-b c1-c c1-6j c1-6k c1-6l c1-6m c1-d c1-e c1-f c1-g")

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            name = listing.find('h4', class_='x-el x-el-h4 c1-1 c1-2 c1-1r c1-1f c1-79 c1-19 c1-17 c1-16 c1-18 c1-7a c1-4y c1-b c1-62 c1-5r c1-47 c1-7b c1-5t c1-5v c1-5w c1-5x').text.strip().split("/22",1)[1]
            desc = 'n/a'
            date = listing.find('h4', class_='x-el x-el-h4 c1-1 c1-2 c1-1r c1-1f c1-79 c1-19 c1-17 c1-16 c1-18 c1-7a c1-4y c1-b c1-62 c1-5r c1-47 c1-7b c1-5t c1-5v c1-5w c1-5x').text.strip().split(" ",1)[0]
            link = "n/a"
            venue = "Cattivo"
            time = "n/a"
            yield Event(name, desc, date, time, link, venue)