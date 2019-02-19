import os, sys

# age = input("How old are you? ")
# height = input("How tall are you? ")
# weight = input("How heavy are you? ")
#
# print(f"So you are {age} years old, {height} tall, and {weight} heavy")

a = ['hello', 'how', 'are', 'you', 'today?', 'sounds', 'great', 'bye']


# print("hello world".__contains__("hello"))
print(a[0:len(a): 3]) #hello today?

print(os.name)

print(sys.argv)

for i in range(len(sys.argv)):
    print(f"Hey this arg is {sys.argv[i]}")
