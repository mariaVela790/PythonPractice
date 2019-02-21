from sys import argv


def create_numbers(num, inc):
    i = 0
    numbers = []

    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += inc

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for number in numbers:
        print(number)


script, user_number, incrementer = argv

create_numbers(int(user_number), int(incrementer))

# i = 0
# numbers = []
#
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i = i + 1
#
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
#
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)

# At the top i is 0
# Numbers now: [0]
# At the bottom i is 1

# At the top i is 1
# Numbers now: [0,1]
# At the bottom i is 2

# ...

# At the top i is 5
# Numbers now: [0, 1, 2, 3, 4, 5]
# At the bottom i is 6

# The numbers
# 0
# 1
# 2
# 3
# 4
# 5
