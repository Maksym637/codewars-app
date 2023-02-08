from implementation.six_kata import SixKata
from utils.features import method_name


class MenuSix:

    def __init__(self):
        self.implementation = SixKata()
    
    @method_name("Rainfall")
    def view_task_1(self):
        pass

    @method_name("Help the bookseller !")
    def view_task_2(self):
        pass

    def get_task_kata_six(self, choice):
        pass

    def run_menu(self):
        pass
