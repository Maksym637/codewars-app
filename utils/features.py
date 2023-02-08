from termcolor import colored


def method_name(name):
    def inner(function):
        def wrapper(*args, **kwargs):
            print(colored(f"\n[ {name} ]\n", "yellow"))
            return function(*args, **kwargs)
        return wrapper
    return inner


def exception_handler(function):
    def wrapper(*args, **kwargs):
        while (True):
            try:
                return function(*args, **kwargs)
            except ValueError as error_description:
                print(colored(f"""\nInvalid input value !\nDescription : [ {
                    error_description
                } ]""", "red"))
    return wrapper
