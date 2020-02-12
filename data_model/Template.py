from data_model.Guest import Guest
from data_model.Company import Company
from datetime import datetime

class Template(object):

    def __init__(self, shortname, template_text):
        self.shortname = shortname
        self.template_text = template_text

    def render_template_string(self, guest, company):
        if not type(guest) == Guest or not type(company) == Company:
            raise TypeError()
            return
        greeting = self.template_text.replace("[timeOfDay]", self._time_of_day()).\
            replace("[firstName]", guest.first_name).\
            replace("[lastName]", guest.last_name).\
            replace("[companyName]", company.company).\
            replace("[roomNumber]", str(guest.reservation.room_number))
        return greeting

    def _time_of_day(self):
        current_time = datetime.now().hour
        if current_time > 17 or current_time < 3:
            return "Evening"
        elif current_time > 11:
            return "Afternoon"
        else:
            return "Morning"

    def __repr__(self):
        return "Template: {}".format(self.shortname)
