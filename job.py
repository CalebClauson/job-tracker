
class Job:
    def __init__(self, company, title, status, date_applied, location, notes, link):
        self.company = company
        self.title = title
        self.status = status
        self.date_applied = date_applied
        self.location = location
        self.notes = notes
        self.link = link

    def to_tuple(self):
        return (self.company, self.title, self.status, self.date_applied, self.location, self.notes, self.link)