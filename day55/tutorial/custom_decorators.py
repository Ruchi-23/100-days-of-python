
# def decorator_function(function):
#     def wrapper_function():
#         function()

#     return wrapper_function

# @decorator_function
# def random_func():
#     pass

def bold_decorator(function):
    def bold_wrapper():
        st = function()
        st = "<h1>" + st + "</h1>"
        return st
    
    return bold_wrapper

def italics_decorator(function):
    def italics_wrapper():
        st = function()
        st = "<em>" + st + "</em>"
        return st
    return italics_wrapper


def underline_decorator(function):
    def underline_wrapper():

        st = function()
        st = "<u>" + st + "</u>"
        return st
    return underline_wrapper