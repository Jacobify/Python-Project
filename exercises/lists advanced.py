front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below:

front_display_list.insert(0,"Pineapple")
print(front_display_list)

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below:

# .pop() is unique in that it will return the value that was removed.


data_science_topics.pop()
data_science_topics.pop(3)
print(data_science_topics)

# Your code below:

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

# Your code below:

range_five_three = range(5, 15, 3)
print("list(range_five_three)")
print(list(range_five_three))

range_diff_five = range(0,40,5)
print(list(range_diff_five))

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)

# Your code below:

long_list_len = len(long_list)
print(long_list_len)

big_range_length = len(big_range)
print(big_range_length)

#---------------------


suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

# Your code below:
print(beginning)

middle  = suitcase[2:4]
print(middle)

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below:

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)
#----------------------------------------

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below:
jake_votes = votes.count("Jake")
print(jake_votes)

#----------------------------------------
# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
# print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
# sort(names)


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(cities)
#------------------------------------------

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)
#------------------------------------------
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len)

first= inventory[0]
last= inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[0:3]

twin_beds = inventory.count("twin bed")

removed_item = inventory.pop(4)

inventory.insert(10,"19th Century Bed Frame")

inventory.sort()

print(inventory)

#Write your function here
def middle_element(lst):
  print(len(lst)/2 - 1)
  if len(lst)%2 == 0:
    return (lst[int(len(lst)/2-1)] +lst[int(len(lst)/2)]) /2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))



#Write your function here
def double_index(lst,index):
  if index >= len(lst):
    return lst
  else:
    new_list = lst[:index]
    new_list.append(lst[index]*2)
    new_list = new_list + lst[index+1:]
    return new_list

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))




#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))




#Write your function here
def every_three_nums(start):
  if start <= 100:
    x = [num for num in range(start,101,3) if num <= 100]
    return x
  else:
    return []

#Uncomment the line below when your function is done
print(every_three_nums(91))