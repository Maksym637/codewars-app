from implementation.seven_kata import SevenKata
from utils.features import method_name


class MenuSeven:

    def __init__(self):
        self.implementation = SevenKata()
    
    @method_name("Looking for a benefactor")
    def view_task_1(self):
        pass

    @method_name("Sum of the first nth term of Series")
    def view_task_2(self):
        pass

    def switch_task(self, choice):
        pass

    def run_menu(self):
        pass
