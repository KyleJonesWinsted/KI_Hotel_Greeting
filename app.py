from data_model.Company import Company
from data_model.Guest import Guest, Reservation
from data_model.Template import Template
from data_model.DataController import DataController

db = DataController()
db.add_file_path('templates', './json/Templates.json')
db.add_file_path('guests', './json/Guests.json')
db.add_file_path('companies', './json/Companies.json')

#Remove these
test_template = db.get_template_by_id(1)
test_company = Company(1, 'Hotel', 'Glencoe', 'east')
test_reservation = Reservation(123, 1234, 1234)
test_guest = Guest(1, 'Kyle', 'Jones', test_reservation)

def main():
    pass

if __name__ == "__main__":
    main()