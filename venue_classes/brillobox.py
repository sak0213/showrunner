from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import ssl
from venue_classes.venue import Venue
from typing import Iterable
from entries import Event
import requests

class Brillobox(Venue):
    @property
    def url(self) -> str:
        return "http://www.brilloboxpgh.com/wp-admin/admin-ajax.php?action=eventorganiser-posterboard&page=1&query%5B0%5D=&query%5Bposts_per_page%5D=10"

    def get_response(self):
        req = requests.get(self.url)
        response = req.json()
        return response

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            name = listing["event_title"]
            desc = 'n/a'
            date = listing['event_start_month'] + " " + listing['event_start_day']
            link = listing['event_permalink']
            venue = "Brillobox"
            time = listing["event_range"].split(" ",-1)[0] + " " + listing["event_range"].split(" ", -1)[1]
            yield Event(name, desc, date, time, link, venue)
