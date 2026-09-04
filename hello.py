#activity 1
print("===========================")
print("Welcome here")
print("My first post!")
print("===========================")

#activity 2 "profile"

username = "cool_creator"
bio= "Fun Blogger"
followers= 100

print("Username:", username)
print("Bio:", bio)
print("Follwers:", followers)

#activity 3 "growth_tracker"

followers = 100

followers +=50
print("Day1:", followers)

followers += 20
print("Day2:", followers)

followers -= 50
print("Day3:", followers)

#activity 4 "interective_profile"

username= input("Enter Username: ")
age= int(input("Enter Age: "))
category=input("Enter Content Category: ")

print("\nInstagram Profile")
print("=====================")
print("Username:", username)
print("Age:", age)
print("Category:", category)

if age>40 and category == "fun":
    print("You are old what is fun for you??")