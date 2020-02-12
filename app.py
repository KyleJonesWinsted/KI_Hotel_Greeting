from data_model.Company import Company
from data_model.Guest import Guest, Reservation
from data_model.Template import Template
from data_model.DataController import DataController
from data_model.UserInterface import UserInterface

db = DataController()
db.add_file_path('templates', './json/Templates.json')
db.add_file_path('guests', './json/Guests.json')
db.add_file_path('companies', './json/Companies.json')

def main():
    print("Press Control+C at any time to exit.\n\n")
    guests = db.get_all_guests()
    companies = db.get_all_companies()
    templates = db.get_all_templates()
    ui = UserInterface(guests, companies, templates)

    ui.main_menu()

if __name__ == "__main__":
    main()