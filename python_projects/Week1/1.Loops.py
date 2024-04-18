# Dogs Loops

dogs = ["boomer", "rocky", "daisy"]

for i in dogs:
    print(i)

print(" ")

for i in range(len(dogs)):
    print(dogs[i])

print(" ")

for i, name in enumerate(dogs):
    print("Number: ", i, "Name: ", name)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(" ")

# Number Loops

sum = 0
for i in numbers:
    sum += i
print("The sum of nums is", sum)
#or
print(f"the sum of nums is {sum}")

print(" ")

#Fncs

def hello(name = "friends"):
    print("hello", name)
hello("Steve")
hello()

print(" ")

#Strings

fname = 'Christian'
lname = "Carreira"
fullname = fname + lname
first_chr = fname[0]
print(first_chr)
last_chr = fname[-1]
print(last_chr)
name_3 = fname*3
print(name_3)

username = 'admin'
if username == 'admin':
    print("Access granted")

full_name = "Christian Carreira"
fname = full_name[0:9]
lname = fullname[9:]
print(fname)
print(lname)

print(" ")

nums = [0, 3, 8, 5, 4]
temp = [0]
temp = nums[2]
nums[2] = nums[4]
nums[4] = temp
print(nums)