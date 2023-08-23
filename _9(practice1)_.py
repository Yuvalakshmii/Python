#q1

def calculate_total_cost(biscuits_available, order_list):
  total_cost = 0
    for biscuit, quantity in order_list. items):
      if biscuit in biscuits_available and quantity <= biscuits_available[biscuit][O]:
        total_cost += quantity * biscuits_available [biscuit] [1]
        biscuits_available [biscuit][0] -= quantity
  return total_cost
# Example usage
biscuits_available = {"Milk Bikis": [10, 10],"Tiger": [5, 5],"Marie": [12, 10],"Dream Cream": [7, 15],"Choco Cream": [5, 15]}
order_list = {"Tiger": 2, "Marie": 1, "Choco Cream": 3}
total_cost = calculate_total_cost(biscuits_available, order_list)
print(total_cost)

#q2
import re
str=input()

if re.match(r"^((?=.*[a-z])(?=.*\d)(?=.*[A-Z])(?=.*?[$#@])[A-Za-z\d$@#]{6,12})$",str):
    print("valid")
else:
    print("invalid")
