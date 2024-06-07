def decorator(func):
    def wrapper():
        print("I am the output that lets you know the function is about to be called.")
        func()
        print("I am the output that lets you know the function has been called.")
    return wrapper

def get_called():
    print("I am the function and I am being called.")


get_called = decorator(get_called)
get_called()

print()

#THE DECORATED VERSION OF CODE (LINES 8 TO 13)
@decorator
def get_called():
    print("I am the function and I am being called.")

get_called()