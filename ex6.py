types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
#Here two strings are put in a string so -2
y = f"Those who know {binary} and those who {do_not}."

hilarious = True

joke_evaluation = "Isn't that joke so funny?! {}"

print(x)
print(y)

#Two more times a string is put in a string
print(f"I said: {x}")
print(f"I also said: '{y}'")

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

#This is an example of string concatenation
print(w + e)