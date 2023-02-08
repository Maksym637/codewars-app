from implementation.seven_kata import SevenKata
from utils.features import method_name, exception_handler
from termcolor import colored


class MenuSeven:

    description = """
        KATA-7 consists with 2 tasks
        Please, choose number 1 or 2
        Enter 0 if you want to go BACK
    """

    def __init__(self):
        self.implementation = SevenKata()
    
    @exception_handler
    @method_name("Looking for a benefactor")
    def view_task_1(self):
        int_arr = list(map(int, input("Enter integer array : ").split()))
        average = float(input("Enter average : "))
        print(f"The benefactor should give = {self.implementation.new_avg(int_arr, average)}")
    
    @exception_handler
    @method_name("Sum of the first nth term of Series")
    def view_task_2(self):
        number = int(input("Enter a number : "))
        print(f"""The sequence of length {number} has a sum = {
            self.implementation.series_sum(number)
        }""")

    def get_task_kata_seven(self, choice):
        switcher = {"1": self.view_task_1, "2": self.view_task_2}

        if choice not in switcher:
            print(colored("\nTask not found !", "red"))
        else:
            return switcher[choice]()

    def run_menu(self):
        while (True):
            print(self.description)
            choice = input("Enter your choice : ")
            if (choice == "0"):
                break
            self.get_task_kata_seven(choice)
