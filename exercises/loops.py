board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for game in sport_games:
  print(game)


promise = "I will finish the python loops module!"

for i in range(5): print(promise)

# ------------------ while loop --------------------------------

# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# Your code below:

countdown = 10
while countdown >=0 :
  print(countdown)
  countdown -= 1
print("We have liftoff!")


# -------------------
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below:
length = len(python_topics)
index =0

while index < length:
  print("I am learning about",python_topics[index])
  index += 1
# ---------------------------------

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)

print(students_period_B)

# ----------------------------------------------------------------

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed  in dog_breeds_available_for_adoption :
  print(dog_breed)
  if dog_breed == dog_breed_I_want :
    print("They have the dog I want!")
    break
# ----------------------------------------------------------------
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21 :
    continue
  else :
    print(age)

# ----------nested-loop----------------
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  for loc in location:
    scoops_sold += loc

print(scoops_sold )

# -------------------------------------------
grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [grade+10 for grade in grades]

print(scaled_grades)
# ------------------------------------------
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
# can_ride_coaster = [height if height > 161 else height > 161 for height in heights]
print(can_ride_coaster)
# -----------------------------------------
# Your code below:
single_digits = range(10)
squares =[]
for digit in single_digits :
  print(digit)
  squares.append(digit**2)
print(squares)


cubes = [digit**3 for digit in single_digits]
print(cubes)


#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#Write your function here
def same_values(lst1,lst2):
  matches =[]
  for index in range(len(lst1)):
      if lst1[index] == lst2[index]:
        matches.append(index)
  return matches

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
def delete_starting_evens(lst):
  while len(lst) >0 and lst[0] % 2 == 0:
     lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
