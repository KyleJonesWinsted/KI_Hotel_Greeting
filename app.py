from data_model.Company import Company
from data_model.Guest import Guest, Reservation
from data_model.Template import Template
from data_model.DataController import DataController
from data_model.UserInterface import UserInterface

ui = UserInterface()

db = DataController()
db.add_file_path('templates', './json/Templates.json')
db.add_file_path('guests', './json/Guests.json')
db.add_file_path('companies', './json/Companies.json')

guests = db.get_all_guests()
companies = db.get_all_companies()
templates = db.get_all_templates()

def main():
    ui.main_menu(guests, companies, templates)

if __name__ == "__main__":
    main()