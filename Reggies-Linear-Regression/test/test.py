
from cmath import inf

possible_bs =[digit/10 for digit in range(-200,201)]
possible_ms =[digit/10 for digit in range(-100,101)]

def get_y(m, b, x):
  y = m*x + b
  return y

def calculate_error(m,b,point):
  x_point,y_point = point
  y = get_y(m,b,x_point)
  distance = abs(y_point-y)
  return distance
def calculate_all_error(m,b,datapoints):
    total_error= 0
    for point in datapoints:
      total =  calculate_error(m,b,point)
      total_error += total
    return total_error
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
smallest_error = inf
best_m = 0
best_b = 0
for m in possible_ms :
	error = calculate_all_error(m,possible_bs[possible_ms.index(m)],datapoints)
	if error <= smallest_error :
		best_m = m
		best_b = possible_bs[possible_ms.index(m)]
		smallest_error = error
