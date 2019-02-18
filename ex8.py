formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

# replaces each {} with the formatter string to get sixteen {}s
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Line one",
    "Line two",
    "Line three",
    "Line four"
))