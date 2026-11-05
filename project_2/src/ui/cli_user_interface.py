"""Contains definition of CliUserInterface class."""

class CliUserInterface:
    """Implements the CliUserInterface class."""

    def __init__(self):
        pass

    def print_menu(self):
        print(f'\t{"Expense Tracker Application"}\n')
        print(f'\t{"1. Create Expense File"}')
        print(f'\t{"2. Load Expense File"}')
        print(f'\t{"3. Export Expense File to CSV"}')
        print(f'\t{"4. Edit Expense Categories"}')
        print(f'\t{"5. Add Expenses"}')
        print(f'\t{"6. Exit"}\n')


    def process_menu_choice(self):
        menu_choice = input("Select Menu Item: ")

        match(menu_choice):
            case "1":
                self.create_expense_file()
               
            case "6":
                exit
            case _: 
                self.invalid_menu_choice()
               


    def create_expense_file(self):
        print(f'{"create_expense_file() method called..."}')

    def invalid_menu_choice(self):
        print(f'{"Invalid menu choice..."}')

    