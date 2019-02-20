def print_two(*args):
    arg1, arg2 = args
    print(f"Here is what you sent in: {arg1} and {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1 : {arg1} and arg2 : {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'")

print_two('hello', 'goodbye')
print_two_again('hello', 'goodbye')

print_one('what is up')
print_none()