# class Event():
#     def __init__(self):
#         self.name = ""
#         self.desc = ""
#         self.date = ""
#         self.time = ""
#         self.link = ""
#
#     @property
#     def entry_output(self):
#         return dict(Name=self.name, Description=self.desc, Date=self.date, Time=self.time, Link=self.link)

from hashlib import sha256


class Event:
    def __init__(self, event_name: str, event_desc: str, event_date: str, event_time: str, event_link: str,
                 event_venue: str):
        self.event_name = event_name
        self.event_desc = event_desc
        self.event_date = event_date
        self.event_time = event_time
        self.event_link = event_link
        self.event_venue = event_venue

    @property
    def id(self):
        return sha256(
            f'{self.event_venue}{self.event_name}{self.event_date}{self.event_time}'.encode('utf-8')).hexdigest()

    def event_output(self) -> dict:
        return {
            'id': self.id,
            'event_name': self.event_name,
            'event_desc': self.event_desc,
            'event_venue': self.event_venue,
            'event_date': self.event_date,
            'event_time': self.event_time,
            'event_link': self.event_link
        }
