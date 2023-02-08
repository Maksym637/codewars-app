from .eight_menu import MenuEight
from .seven_menu import MenuSeven
from .six_menu import MenuSix


class MenuDelegator:

    description = """
        some text
    """

    def run_program(self):
        while(True):
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
                print("Kata not found !")
