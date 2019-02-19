days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#These are going to print the values
print("Here are the days: ", days)
print("Here are the months: ", months)

#This is going to print a long line of text
print("""
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5 or 6.
""")

print("""
    Mary had a little lamb.
    It's fleece was white as {}
    And everywhere that Mary went.
    {}
""".format('snow', '.' * 10))
