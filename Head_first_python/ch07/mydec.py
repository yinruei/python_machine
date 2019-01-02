
def print_my_name(name):
    print("I am %s "%(name()))
    # return name # return 傳進來的 function

@print_my_name
def my_name():
    return "Hans"


# ---------------------------------------------------------------
# def print_my_name(name):
#     print("I am " + name())

# def my_name():
#     return "Hans"

# my_name = print_my_name(my_name)
