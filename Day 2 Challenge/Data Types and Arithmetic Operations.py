# 1. Check the data type of all your variables using type() built-in function
first_name = "Tosan"
last_name = "Gbiaye"
full_name = first_name + ' ' + last_name
print(full_name)
country = "Nigeria"
city = "Lagos"
age = 25
year = 2022
is_married = False
print(type(first_name))
print(type(country))
print(type(age))
print(type(is_married))
print(type(2 + 7j))
print(type(False))
print(type([1,2,4,9]))
print(type({'name': 'Tosan', 'age': 25, 'occupation': 'Test Automation Engineer'}))
print(type(39.7))
print(type((1,2,3)))
print(type(([1,2],[3,4])))
print(type(zip([1,2],[3,4])))

# 2. Using the len() built-in function, find the length of your first name
print(len(first_name))
# 3. Compare the length of your first name and your last name
print(len(last_name))
# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# i. Add num_one and num_two and assign the value to a variable total
total_sum = num_one + num_two
print(total_sum)
# ii. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)
# iii. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)
# iv. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)
# v.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
modulus = num_one % num_two
print(modulus)
# vi. Calculate num_one to the power of num_two and assign the value to a variable exp
exp =num_one ** num_two
print(exp)
# vii. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

# 5. The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
pi = 3.14
area_of_circle = pi * radius * radius
print(area_of_circle)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * radius
print(circum_of_circle)
# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('What is your first_name: ')
last_name = input('What is your last_name: ')
country = input('Enter your country: ')
age = input('How old are you: ')
print(first_name)
print(last_name)
print(country)
print(age)
