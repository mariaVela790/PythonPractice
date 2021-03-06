from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
# in_file = open(from_file, 'r').read()
# in_file = open(from_file)
# indata = in_file.read()

# print(f"""
# The input file is {len(indata)} bytes long
# Does the output file exist? {exists(to_file)}
# Ready, hit RETURN to continue, CTRL - C to abort.
# """)

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print("Alright, all done.")
# out_file.close()
# in_file.close()

with open(from_file, 'r') as in_file:
    indata = in_file.read()

with open(to_file, 'w') as out_file:
    out_file.write(indata)
