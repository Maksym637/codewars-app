from implementation.six_kata import SixKata
from utils.features import method_name, exception_handler, read_file
from utils.constants import FILE_PATH_1, FILE_PATH_2
from termcolor import colored


class MenuSix:

    description = """
        KATA-6 consists with 2 tasks
        Please, choose number 1 or 2
        Enter 0 if you want to go BACK
    """

    def __init__(self):
        self.implementation = SixKata()
    
    @exception_handler
    @method_name("Rainfall")
    def view_task_1(self):
        choice = input("Enter 1 or 2 to see rainfall records : ")
        rainfall_data = read_file(FILE_PATH_1) if choice == "1" else read_file(FILE_PATH_2)
        print(f"\n{rainfall_data}\n")
        town = input("Enter town name for which calculation will be made : ")
        print(f"""Mean is = {self.implementation.mean(town, rainfall_data)}, Variance is = {
                self.implementation.variance(town, rainfall_data)
        }""")

    @exception_handler
    @method_name("Help the bookseller !")
    def view_task_2(self):
        books = input("Enter the book's category and quantity\nPlease, separate new book with ',' : ").split(",")
        categories = input("Enter a list of categories in capital letters : ").split()
        print(f"The help result is : {self.implementation.stock_list(books, categories)}")

    def get_task_kata_six(self, choice):
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
            self.get_task_kata_six(choice)
