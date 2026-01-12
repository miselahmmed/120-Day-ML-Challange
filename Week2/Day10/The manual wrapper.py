def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper
@my_decorator
def say_hello():
    print("Hello World!")
say_hello()