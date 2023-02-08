from .eight_menu import MenuEight
from .seven_menu import MenuSeven
from .six_menu import MenuSix
from termcolor import colored


class MenuDelegator:

    description = """
          ALL KATAS

        1.) KATA - 8
        2.) KATA - 7
        3.) KATA - 6

        Enter 0 to exit.
    """

    def run_program(self):
        print(colored("\n\tWelcome to menu !", "yellow"))
        while (True):
            print(self.description)
            choice = input("Enter your choice : ")
            if (choice == "1"):
                MenuEight().run_menu()
            elif (choice == "2"):
                MenuSeven().run_menu()
            elif (choice == "3"):
                MenuSix().run_menu()
            elif (choice == "0"):
                exit(0)
            else:
                print(colored("\nKata not found !", "red"))
