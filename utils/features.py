def method_name(name):
    def inner(function):
        def wrapper(*args, **kwargs):
            print(f"[ {name} ]")
            return function(*args, **kwargs)
        return wrapper
    return inner
