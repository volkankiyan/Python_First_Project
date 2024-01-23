# Write your code here
# print("""Prices:
# Bubblegum: $2
# Toffee: $0.2
# Ice cream: $5
# Milk chocolate: $4
# Doughnut: $2.5
# Pancake: $3.2""")

print("""
Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80""")
total = 202 + 118+ 2250 + 1680 + 1075+80
print("Income: $" +str(total))
print("Staff expenses:")
exp1 = int(input())
print("Other expenses")
exp2 = int(input())
print("Net income: $" + str((total - (exp1 + exp2))))