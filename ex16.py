from sys import argv

script, filename = argv

print(f"""
We're going to erase {filename}
If you don't want that, hit CTRL - C (^C)
If you do want that, hit RETURN
""")

input("?")

print("Opening the file...")
target = open(filename, 'w')

# We don't need to truncate the file because the mode 'w' begins
# by truncating the file
# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for the three lines")

# line1 = input("line 1: ")
# line2 = input("line 2: ")
# line3 = input("line 3: ")
line = input("line 1: ") + "\n" + input("line 2: ") + "\n" + input("line 3: ")

print("I'm going to write these to the file.")

target.write(line)
# target.write()

# target.write(line1)
# target.write("\n")
#
# target.write(line2)
# target.write("\n")
#
# target.write(line3)
# target.write("\n")

# print(target.read())

print("And finally, we close it.")
target.close()


