from sys import argv

script, filename = argv

#retrieves file object
txt = open(filename)

print(f"Here's your file {filename}")
#calls read method on the file object we recieved
print(txt.read())

print("Type the filename again")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())