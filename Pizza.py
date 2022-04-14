print("Welcome to my Pizzeria!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
age = int(input("What is your age? "))

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1

if age >= 45 and age <= 55:
  print('Have a nice day, your pizza is on us!')
else:

  print(f"Your final bill is ${bill}")
