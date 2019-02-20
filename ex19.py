def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"""You have {cheese_count} cheeses!
    You have {boxes_of_crackers} boxes of crackers!
    Man that's enough for a party!
    Get a blanket
    """)


def hello_and_goodbye(person_name, age):
    print(f""" 
    Hello {person_name}! I can't believe you're already {age}!
    Goodbye now :)
    """)


print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# ////////////////////running hello_and_goodbye

hello_and_goodbye('Maria', 1)
hello_and_goodbye('Maria', '2')

my_name = 'Maria'
hello_and_goodbye(my_name, 1 + 2)

hello_and_goodbye(4, 'Maria')
hello_and_goodbye('Maria' + my_name, 4 + 1)

hello_and_goodbye(f"{my_name}", 6)
# hello_and_goodbye()


def sum_nums(num1, num2):
    return num1 + num2


print(sum_nums(5, 4))
prompt = "enter a number: "
print(sum_nums(int(input(prompt)), int(input(prompt))))