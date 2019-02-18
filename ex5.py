#In this program we will be learning about formatting strings
#to format we put an f in front of the string and insert variables
#using curly braces {} one example is the following:
# f"Here is a string with the number {5}"

message = f"Here is a string with the number {5}"
my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
rate_for_in_to_cm = 2.54
rate_for_lbs_to_kg = round(.45)

print(rate_for_lbs_to_kg)

print(message)
print(f"Let's talk about {my_name}") #Let's talk about Zed A. Shaw
print(f"He's {my_height} inches tall") #He's 74 inches tall
print(f"He's {my_height * rate_for_in_to_cm} centimeters tall") #He's {converted amount} inches tall
print(f"He's {my_weight} pounds heavy.") #He's 180 pounds heavy
print(f"He's {my_weight * rate_for_lbs_to_kg} kg heavy.") #He's 180 pounds heavy
print("Actually that's not too heavy.") #Actually that's not too heavy
print(f"He's got {my_eyes} eyes and {my_hair} hair.") #He's got Blue eyes and Brown hair
print(f"His teeth are usually {my_teeth} depending on the coffee.") #His teeth are usually White depending on the coffee

#This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
#If I add 35, 74, and 180 I get 289