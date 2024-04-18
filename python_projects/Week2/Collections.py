#Lists

list = [10,20,30,40,50]
list.append(5)
list.append(6)
list.append(7)
print(list)

list.remove(40)
list.pop(2)
print(list)

list.reverse()
print(list)
list.sort()
print(list)

list[0] = 500
print(list)

list = list[1:]
print(list)

index10 = list.index(10)
print(index10)

list.append(20)
list.append(20)
list.append(20)
print(list)

"""
HW2 Problem
"""
count20 = list.count(20)
print(count20)

copy_list = list
print(copy_list)
copy_list[0] = 99
print(copy_list)

new_copy = list.copy()
print(new_copy)
new_copy[0] = 500
print(new_copy)
print(list)

new_copy = list[:]

empty_list = []
for val in list:
    empty_list.append(val)
print(empty_list)

empty_list = [0] * 10
print(empty_list)
empty_list[0] = 10

squares = []
for val in range(1,10):
    squares.append(val*val)
print(squares)

plus_5 = [val + 5 for val in list]
print(plus_5)

small_vals = [val for val in list if val < 20]
print(small_vals)

#Dictionaries
fav_foods = {"Kathleen" : "pizza", "Hannah" : "pasta", "Kush" : "fries", "Yamill" : "fries"}
print(fav_foods)
hff = fav_foods["Hannah"]
print(hff)

for key in fav_foods:
    print(f"{key}'s favorite food is {fav_foods[key]}")

for person, food in fav_foods.items():
    print(f"{person}'s favorite food is {food}")

#bff = fav_foods["Bob"] Error
if "Bob" in fav_foods:
    print(fav_foods["Bob"])
else:
    fav_foods["Bob"] = "wings"
print(fav_foods)