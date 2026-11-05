""" Main Entry Point """

from ui.cli_user_interface import CliUserInterface

def main():
   cli_ui = CliUserInterface()
   cli_ui.print_menu()
   cli_ui.process_menu_choice()


if __name__ == "__main__":
    main()