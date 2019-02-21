print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("""This door leads to Narnia! Choose to:
    1. Talk to a fawn
    2. Ride a unicorn
    3. Play in the snow""")

    choice = input("> ")

    if choice == "1":
        print("He told you about a cool party and you had fun going!")
    elif choice == "2":
        print("The unicorn took you to another magical land!")
    elif choice == "3":
        print("You froze to death")
    else:
        print("Welp, you failed.")

elif door == "2":
    print("""This door leads to your closest so you can choose an outfit for the day.
    1. Raincoat and rain boots
    2. Sundress
    3. T-shirt and jeans""")

    outfit = input("> ")

    if outfit == "1":
        print("It's sunny")
    elif outfit == "2":
        print("It's rainy")
    elif outfit == "3":
        print("Yay perfect outfit for coding!")
    else:
        print("You wore no clothes and it's emburussing")

else:
    print("So indecisive!")
# if door == "1":
#     print("""There's a giant bear here eating a cheese cake
#     What do you do?
#     1. Take the cake.
#     2. Scream at the bear.""")
#
#     bear = input("> ")
#
#     if bear == "1":
#         print("The bear eats your face off. Good job!")
#     elif bear == "2":
#         print("The bear eats your legs off. Good job!")
#     else:
#         print(f"Well, doing {bear} is probably better.")
#         print("Bear runs away.")
#
# elif door == "2":
#     print("""You stare into the endless abyss at Cthulhu's retina.
#     1. Blueberries.
#     2. Yellow jacket clothespins.
#     3. Understanding revolvers yelling melodies.""")
#
#     insanity = input("> ")
#
#     if insanity == "1" or insanity == "2":
#         print("Your body survives powered by a mind of jello.")
#     else:
#         print("The insanity rots your eyes into a pool of muck.")
#         print("Good job!")
#
# else:
#     print("You stumble around fall on a knife and die. Good job!")
#
