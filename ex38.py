ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ") # stuff = ["Apples", "Oranges", "Crows", "Telephone", "Light", "Sugar"]
# split(ten_things, " ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# len(stuff) == 6
while len(stuff) != 10:
    # pop(more_stuff)
    next_one = more_stuff.pop()  # "Boy"
    print("Adding: ", next_one)  # Adding Boy
    # append(stuff, next_one)
    stuff.append(next_one)
    # stuff --> ["Apples", "Oranges", "Crows", "Telephone", "Light", "Sugar", "Boy", "Girl", "Banana", "Corn"]
    print(f"There are {len(stuff)} items now.")  # There are 7 items


print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])  # Oranges
print(stuff[-1])  # Corn
# pop(stuff)
print(stuff.pop())  # Corn
# join(' ', stuff)
print(' '.join(stuff)) # "Apples Oranges Crows Telephone Light Sugar Boy Girl Banana"
# join('#', stuff([3:5]))
print('#'.join(stuff[3:5]))  # "Telephone#Light"
