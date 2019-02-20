from sys import argv

script, filename = argv

#retrieves file object
txt = open(filename)

print(f"Here's your file {filename}")
#calls read method on the file object we recieved
print(txt.read())

print("Edit the file by typing in what you want to add:")
edit = input('> ')

txt.write(f'{edit}')


txt.close()