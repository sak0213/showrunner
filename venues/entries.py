class Event():
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.date = ""
        self.time = ""
        self.link = ""

    @property
    def entry_output(self):
        return dict(Name=self.name, Description=self.desc, Date=self.date, Time=self.time, Link=self.link)
