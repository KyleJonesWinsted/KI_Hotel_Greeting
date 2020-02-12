import sys
from data_model.Template import Template

class UserInterface(object):

    """
    Program executes in the following order
    Select template or custom greeting ->
    Select/Enter greeting ->
    Select company ->
    Select guest ->
    Greeting is sent and program restarts
    """

    def __init__(self, guests, companies, templates):
        self.guests = guests
        self.companies = companies
        self.templates = templates

        self.current_greeting = None
        self.current_guest = None
        self.current_company = None

    #Ensures user input is an int and within the range of options, else asks for input again
    def _get_user_int_input(self, user_prompt, menu, number_of_options):
        try:
            user_input = int(input(user_prompt))
            if user_input > number_of_options or user_input < 1:
                raise Exception
            return user_input
        except Exception:
            print("\nInvalid input please enter the number that corresponds to your choice.")
            menu()
        except KeyboardInterrupt:
            print('\n')
            if menu == self.main_menu:
                sys.exit()
            else:
                self.main_menu()

    def main_menu(self):
        print("\nWelcome! Please select an option below.")
        self._enumerate_options([
            "Select Preset Greeting",
            "Send Custom Greeting"
        ])
        user_input = self._get_user_int_input("> ", self.main_menu, 2)
        if user_input == 1:
            self._select_greeting()
        elif user_input == 2:
            self._custom_greeting()

    def _select_greeting(self):
        print("\nSelect the greeting you would like to send.")
        self._enumerate_options([
            template.shortname for template in self.templates
        ])
        user_input = self._get_user_int_input("> ", self._select_greeting, len(self.templates))
        self.current_greeting = self.templates[user_input - 1]
        self._select_company()

    def _custom_greeting(self):
        print("\nEnter your custom greeting. You can use the following placeholders: ")
        placeholders = {
            "timeOfDay": "Inserts Morning, Evening, or Afternoon",
            "firstName": "Inserts Guest's First Name",
            "lastName": "Inserts Guest's Last Name",
            "roomNumber": "Inserts the Reserved Room Number",
            "companyName": "Inserts the Hotel's Name"
        }
        for key, value in placeholders.items():
            print("[{}] - {}".format(key, value))
        print("\nBe sure to include the square brackets in your greeting placeholders.\n")
        try:
            user_input = input("> ")
        except KeyboardInterrupt:
            self.main_menu()
        custom_template = Template(
            id = 99,
            shortname = "Custom Greeting",
            template_text = user_input.strip()
        )
        self.current_greeting = custom_template
        self._select_company()


    def _select_company(self):
        print("Select your company: ")
        self._enumerate_options([
            company.company for company in self.companies
        ])
        user_input = self._get_user_int_input("> ", self._select_company, len(self.companies))
        self.current_company = self.companies[user_input - 1]
        self._select_guest()

    def _select_guest(self):
        print("Select the guest to greet: ")
        self._enumerate_options([
            guest.full_name() for guest in self.guests
        ])
        user_input = self._get_user_int_input("> ", self._select_guest, len(self.guests))
        self.current_guest = self.guests[user_input - 1]
        self._send_greeting()

    def _send_greeting(self):
        print("\nSent greeting to {}\n".format(self.current_guest.full_name()))
        print(self.current_greeting.render_template_string(self.current_guest, self.current_company))
        
        self.current_company = None
        self.current_guest = None
        self.current_greeting = None

        self.main_menu()

    #Prints all options in options list along with a corresponding number
    def _enumerate_options(self, options):
        print("")
        for i, option in enumerate(options):
            print("[ {} ] {}".format(i + 1, option))
        print("")
