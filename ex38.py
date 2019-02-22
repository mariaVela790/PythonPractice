ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ") # stuff = ["Apples", "Oranges", "Crows", "Telephone", "Light", "Sugar"]
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# len(stuff) == 6
while len(stuff) != 10:
    next_one = more_stuff.pop()  # "Boy"
    print("Adding: ", next_one)  # Adding Boy
    stuff.append(next_one)
    # stuff --> ["Apples", "Oranges", "Crows", "Telephone", "Light", "Sugar", "Boy", "Girl", "Banana", "Corn"]
    print(f"There are {len(stuff)} items now.")  # There are 7 items


print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])  # Oranges
print(stuff[-1])  # Corn
print(stuff.pop())  # Corn
print(' '.join(stuff)) # "Apples Oranges Crows Telephone Light Sugar Boy Girl Banana"
print('#'.join(stuff[3:5]))  # "Telephone#Light"