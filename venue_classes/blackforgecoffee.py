import json
import re
from venue_classes.venue import Venue
from typing import Iterable
from entries import Event
import requests
from datetime import datetime

class BlackForge(Venue):
    @property
    def url(self) -> str:
        return "https://shy.elfsight.com/p/boot/?a=&callback=__esappsPlatformBoot1657041128348&shop=black-forge-coffee.myshopify.com&w=96e6324b-f1c0-435b-85f8-4e9d064e7589"

    def get_response(self):
        request = requests.get(self.url)
        response = request.text
        data = json.loads(re.search('({.+})', response).group(0))
        return data['data']['widgets']['96e6324b-f1c0-435b-85f8-4e9d064e7589']['data']['settings']['events']

    def get_events(self) -> Iterable[Event]:
        event_data = self.get_response()
        for listing in event_data:
            name = listing['name']
            desc = listing['description']
            try:
                source_date = listing['start'] /1000
                date = datetime.fromtimestamp(source_date, tz=None).date()
                date = str(date)
            except:
                date = listing['start']
            time = listing['start']
            link = 'n/a'
            venue = 'BlackForge'

            yield Event(name, desc, date, time, link, venue)