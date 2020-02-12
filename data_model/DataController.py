import json
from data_model.Template import Template
from data_model.Guest import Guest, Reservation
from data_model.Company import Company

class DataController(object):

    def __init__(self):
        self.file_paths = {}

    def add_file_path(self, path_name, file_path):
        self.file_paths[path_name] = file_path

    def _get_file_path(self, path_name):
        try:
            file_path = self.file_paths[path_name]
            return file_path
        except:
            raise FileException("No file path for {}".format(path_name))

    def _load_json(self, path_name):
        file_path = self._get_file_path(path_name)
        with open(file_path) as json_file:
            data = json.load(json_file)
            return data

    def get_all_templates(self):
        templates = []
        data = self._load_json('templates')
        for template in data:
            new_template = Template(
                id = template['id'],
                shortname = template['shortName'],
                template_text = template['templateText']
            )
            templates.append(new_template)
        return templates

    def get_all_guests(self):
        guests = []
        data = self._load_json('guests')
        for guest in data:
            reservation_json = guest['reservation']
            new_reservation = Reservation(
                room_number = reservation_json['roomNumber'],
                start_timestamp = reservation_json['startTimestamp'],
                end_timestamp = reservation_json['endTimestamp']
            )
            new_guest = Guest(
                id = guest['id'],
                first_name = guest['firstName'],
                last_name = guest['lastName'],
                reservation = new_reservation
            )
            guests.append(new_guest)
        return guests

    def get_all_companies(self):
        companies = []
        data = self._load_json('companies')
        for company in data:
            new_company = Company(
                id = company['id'],
                company = company['company'],
                city = company['city'],
                timezone = company['timezone']
            )
            companies.append(new_company)
        return companies

    def add_new_template(self, template):
        template_json = template.serialize()
        file_path = self._get_file_path('templates')
        with open(file_path, mode='r') as json_file:
            data = json.load(json_file)
        data.append(template_json)
        with open(file_path, mode='w') as json_file:
            json_file.write(json.dumps(data, indent=4))
            

class FileException(Exception):
    pass