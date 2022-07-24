ints_and_strings = [1, 2, 3, "four", "five","why so serious"]

sam_height_and_testscore = ["Sam",67 , 85.5 , True]

print(sam_height_and_testscore)

heights = [61, 70, 67, 64,65]

broken_heights = [65 , 71 , 59 , 62]

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
print(example_list)

#Using Remove
example_list.remove(2)
print(example_list)

orders = ["daisies", "periwinkle"]

print(orders)

orders.append("tulips")
orders.append("roses")

print(orders)

# concatation
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac","iris"]
orders_combined = orders + new_orders

broken_prices = [5, 3, 4, 5, 4] + [4]