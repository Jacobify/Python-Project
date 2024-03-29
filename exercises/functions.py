# Your code below:
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")


# Your code below:
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit",location)
  print("You can use the public subway system to get to",location)

generate_trip_instructions("Grand Central Station")

# Write your code below:
def calculate_expenses(plane_ticket_price,car_rental_rate,hotel_rate,trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print(car_rental_total+hotel_total +plane_ticket_price)

calculate_expenses(200,100,100,5)

# Write your code below:

def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner("Brooklyn", "Queens")

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:

max_price = max(tshirt_price,
shorts_price,
mug_price,
poster_price)
min_price = min(tshirt_price,
shorts_price,
mug_price,
poster_price)
rounded_price = round(tshirt_price,1)
print(max_price)
print(min_price)
print(rounded_price)


# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland"

def print_count_locations():
  print("There are 3 locations")

# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below:
shirt_expense =9
def deduct_expense(budget,expense):
  return budget - expense

new_budget_after_shirt =  deduct_expense(current_budget,shirt_expense)

print_remaining_budget(new_budget_after_shirt)
# -------------------------------------------------
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first,second,third

most_popular1,most_popular2,most_popular3 =  top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)
# -----------------------------------------------
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0",name)

trip_planner_welcome("Farzad")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(24.6)

def destination_setup(origin,destination,estimated_time,mode_of_transport="Car"):
  print("Your trip starts off in",origin)
  print("And you are traveling to",destination)
  print("You will be traveling by",mode_of_transport)
  print("It will take approximately",estimated_time,"hours")

destination_setup("Mashhad","Vida",estimate)

# ------------------------------------------------
# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# Write your code below:

def f_to_c(f_temp) :
  c_temp =( f_temp - 32 ) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)


def c_to_f(c_temp) :
  f_temp = c_temp * (9/5) +32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass,acceleration) :
  return mass*acceleration

train_force = get_force(train_mass,train_acceleration)
print("The GE train supplies",train_force,"Newtons of force.")


def get_energy(mass,c =3*10**8 ):
  return mass*c**2

bomb_energy= get_energy(bomb_mass)
print("A 1kg bomb supplies",bomb_energy/10**12,"Terra Joules.")



def get_work(mass,acceleration,distance):
  return get_force(mass,acceleration)*distance

train_work =  get_work(train_mass,train_acceleration,train_distance)
print("The GE train does",train_work/1000,"Kilo Joules of work over",train_distance,"meters.")