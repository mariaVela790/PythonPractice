from sys import argv

script, filename = argv

#retrieves file object
txt = open(filename)

print(f"Here's your file {filename}")
#calls read method on the file object we recieved
print(txt.read())
