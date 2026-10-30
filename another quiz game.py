# Write code below 💖

houses = {
    "Gryffindor": 0,
    "Ravenclaw": 0,
    "Hufflepuff": 0,
    "Slytherin": 0
}

# Question 1
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

answer = int(input("Enter your choice: "))

if answer == 1:
    houses["Gryffindor"] += 1
    houses["Ravenclaw"] += 1
elif answer == 2:
    houses["Hufflepuff"] += 1
    houses["Slytherin"] += 1
else:
    print("Wrong input.")


# Question 2
print("\nQ2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

answer = int(input("Enter your choice: "))

if answer == 1:
    houses["Hufflepuff"] += 2
elif answer == 2:
    houses["Slytherin"] += 2
elif answer == 3:
    houses["Ravenclaw"] += 2
elif answer == 4:
    houses["Gryffindor"] += 2
else:
    print("Wrong input.")


# Question 3
print("\nQ3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

answer = int(input("Enter your choice: "))

if answer == 1:
    houses["Slytherin"] += 4
elif answer == 2:
    houses["Hufflepuff"] += 4
elif answer == 3:
    houses["Ravenclaw"] += 4
elif answer == 4:
    houses["Gryffindor"] += 4
else:
    print("Wrong input.")


# Print scores
print("\nScores:")

for house in houses:
    print(house + ":", houses[house])