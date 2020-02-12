class Company(object):

    def __init__(self, id, company, city, timezone):
        self.id = id
        self.company = company
        self.city = city
        self.timezone = timezone

    def __repr__(self):
        return "Company(id: {}, name: {}".format(self.id, self.company)