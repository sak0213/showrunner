from venue_classes.venue import Venue
from typing import Iterable
from entries import Event
import requests
from datetime import datetime

class Spirit(Venue):
    @property
    def url(self) -> str:
        return "https://www.spiritpgh.com/api/open/GetItemsByMonth?month=07-2022&collectionId=5511e880e4b0b2a9ab8e61bf&crumb=BevUHMaRFR2FMjc5MWVlMjBlYzEwMzNiMTA5MTE3ZmI5ODhlODU2"

    def get_response(self):
        req = requests.get(self.url)
        response = req.json()
        return response

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            name = listing['title']
            desc = 'n/a'
            try:
                source_date = listing['startDate']
                date = datetime.fromtimestamp(source_date / 1000).date()
                date = str(date)
            except:
                date = listing['startDate']
            link = "https://www.spiritpgh.com/" + listing['fullUrl']
            venue = "Spirit"
            time = listing['startDate']

            yield Event(name, desc, date, time, link, venue)