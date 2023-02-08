from implementation.eight_kata import EightKata
from utils.features import method_name


class MenuEight:

    description = """
        KATA-8 consists with 8 tasks
        Please, choose number from 1 to 8
        Enter 0 if you want to exit
    """
    
    def __init__(self):
        self.implementation = EightKata()
    
    @method_name("Keep Hydrated!")
    def view_task_1(self):
        time = float(input("Enter time : "))
        print(f"Liters = {self.implementation.liters(time)}")

    @method_name("Volume of a Cuboid")
    def view_task_2(self):
        length, width, height = map(float, input("Enter length, width and height : ").split())
        print(f"Volume of Cuboid = {self.implementation.get_volume_of_cuboid(length, width, height)}")

    @method_name("Miles per gallon to kilometers per liter")
    def view_task_3(self):
        mpg = float(input("Enter miles per imperial gallon : "))
        print(f"Kilometers per liter = {self.implementation.converter(mpg)}")

    @method_name("To square(root) or not to square(root)")
    def view_task_4(self):
        int_arr = list(map(int, input("Enter integer array : ").split()))
        print(f"Procecced array = {self.implementation.square_or_square_root(int_arr)}")

    @method_name("Count of positives/sum of negatives")
    def view_task_5(self):
        int_arr = list(map(int, input("Enter integer array : ").split()))
        print(f"""[count of positives numbers, sum of negative numbers] = {
            self.implementation.count_positives_sum_negatives(int_arr)
        }""")

    @method_name("Convert a String to a Number!")
    def view_task_6(self):
        str_number = str(input("Enter a number : "))
        print(f"""Type of entered number = {type(str_number)} | Type of output number = {
            type(self.implementation.string_to_number(str_number))
        }""")

    @method_name("Formatting decimal places")
    def view_task_7(self):
        number = float(input("Enter a number : "))
        print(f"{number} is rounded {self.implementation.two_decimal_places(number)}")

    @method_name("Find numbers which are divisible by given number")
    def view_task_8(self):
        int_arr = list(map(int, input("Enter integer array : ").split()))
        divisor = int(input("Enter divisior : "))
        print(f"""Numbers {int_arr} which are divisible by {divisor} are : {
            self.implementation.divisible_by(int_arr, divisor)
        }""")
    
    def switch_task(self, choice):
        switcher = {
            "1": self.view_task_1, "2": self.view_task_2,
            "3": self.view_task_3, "4": self.view_task_4,
            "5": self.view_task_5, "6": self.view_task_6,
            "7": self.view_task_7, "8": self.view_task_8
        }

        if choice not in switcher:
            print("Task not found !")
        else:
            return switcher[choice]()
    
    def run_menu(self):
        while(True):
            print(self.description)
            choice = input("Enter your choice : ")
            if (choice == "0"):
                break
            self.switch_task(choice)
