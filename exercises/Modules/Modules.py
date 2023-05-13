# Import datetime from datetime below:
from datetime import datetime

current_time = datetime.now()

print(current_time)

# Import random below:
import random

# Create random_list below:
random_list = []

for i in range(101):
  random_list.append(random.randint(1,101))


# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

# namespaces
#import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random
# Add your code below:

numbers_a = range(1,13)
numbers_b = random.sample(numbers_a,12)
print(numbers_b)
plt.plot(numbers_a,numbers_b)
plt.show()
