print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')


poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("----------------")
print(poem)
print("----------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# This next line calls the function to the values and assign them to beans, jars, crates
beans, jars, crates = secret_formula(start_point)

#
# print("With a starting point of: {}".format(start_point))
#
# print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
#
# # start_point = start_point / 10
#
# print("We can also do that this way:")
# # This one assigns the values in a different
# # formula = secret_formula(start_point)
#
# print("We'd have {} beans, {} jars, and {} crates.".format(*secret_formula(start_point / 10)))

print(f"""
With a starting point of: {start_point}
We'd have {beans} beans, {jars} jars, and {crates} crates.
We can also do that this way:
""")

print("We'd have {} beans, {} jars, and {} crates.".format(*secret_formula(start_point/10)))