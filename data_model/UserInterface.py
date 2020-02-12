class UserInterface(object):

    def __init__(self, guests, companies, templates):
        self.guests = guests
        self.companies = companies
        self.templates = templates

    def get_user_int_input(self, user_prompt, menu, number_of_options):
        try:
            user_input = int(input(user_prompt))
            if user_input > number_of_options:
                raise Exception
            return user_input
        except Exception:
            print("\nInvalid input please enter the number that corresponds to your choice.")
            menu()
        except KeyboardInterrupt:
            print('\n')
            return

    def main_menu(self):
        print("\nWelcome! Please select an option below.")
        self._enumerate_options([
            "Select Preset Greeting",
            "Send Custom Greeting"
        ])
        user_input = self.get_user_int_input("Enter a number: ", self.main_menu, 2)
        if user_input == 1:
            send_greeting()
        elif user_input == 2:
            create_greeting()

    def send_greeting(self):
        print("Select the greeting you would like to send.")
        self._enumerate_options([
            template. for template in self.templates
        ])

    def create_greeting(self):
        pass


    def _enumerate_options(self, options):
        for i, option in enumerate(options):
            print("[ {} ] {}".format(i + 1, option))
