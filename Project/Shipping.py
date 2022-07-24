weight = 1.5
# Ground Shipping
ground_Shipping_cost = 0
if weight <= 2:
  ground_Shipping_cost = weight*1.5 + 20
elif weight > 2 and weight <=6:
  ground_Shipping_cost = weight*3 + 20
elif weight > 6 and weight <=10:
  ground_Shipping_cost = weight*4 + 20
elif weight > 10:
  ground_Shipping_cost = weight*4.75 +20

print("Ground shipping cost is : ",ground_Shipping_cost)

# premium ground shipping cost

premium_ground_shipping_cost =125

print("Primium ground shipping cost is : ",premium_ground_shipping_cost)

# Drone Shipping

drone_Shipping_cost = 0
if weight <= 2:
  drone_Shipping_cost = weight*4.5
elif weight > 2 and weight <=6:
  drone_Shipping_cost = weight*9
elif weight > 6 and weight <=10:
  drone_Shipping_cost = weight*12
elif weight > 10:
  drone_Shipping_cost = weight*14.25

print("Drone shipping cost is : ",drone_Shipping_cost)


