import math
shopping = [10,20,30]
item_average = len(shopping)
item_total = 0

for items in range(len(shopping)):
    item_total += shopping[items]

item_total_average = item_total/item_average
print(item_total_average)