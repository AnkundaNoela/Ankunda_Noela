#EXERCISE 1
# Exercise 1: Create a list and output the 2nd item
names = ["Noela","Tracy", "Bocker", "Bridget", "Vennie"]
print("second item",names[1])

# Exercise 2: Change the value of the first item
names[0] = "Ankunda"
print("changed value of the first item to", names[0] )

# Exercise 3: Add a sixth item to the list
names.append("Bree")
print("new list", names)

# Exercise 4: Add "Hillary" as the 3rd item
names.insert(2,"Hillary")
print("updated list", names)

# Exercise 5: Remove the 4th item from the list
del names[3]
print("updated list", names)

# Exercise 6: Use negative indexing to print the last item
print("Last item:", names[-1])

# Exercise 7: Create a new list and print 3rd to 5th items
new_list = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink"]
print("3rd to 5th items:",new_list[2:5])

# Exercise 8: Copy a list of countries
countries=["Kenya", "Uganda", "Tanzania", "Rwanda"]
countries_copy = countries.copy()
print("Copied countries list:", countries_copy)

# Exercise 9: Loop through the list of countries
print("Loop through countries:")
for country in countries:
    print(country)
    
# Exercise 10: Sort animal names in ascending and descending order
animals = ["Zebra", "Elephant", "Lion", "Giraffe", "Antelope", "Cheetah"]
animals_sorted_asc = sorted(animals)
animals_sorted_desc = sorted(animals, reverse=True)
print("Ascending order:", animals_sorted_asc)
print("Descending order:", animals_sorted_desc)

# Exercise 11: Output animal names with letter 'a'
print("Animals with 'a':")
for animal in animals:
    if 'a' in animal.lower():
        print(animal)
        
# Exercise 12: Join two lists of first names and second names
first_names = ["Atukunda", "Agaba", "Ashaba"]
second_names = ["Bridget", "Hillary", "Eugene"]
full_names = first_names + second_names
print("Joined names:", full_names)        

#EXERCISE 2
# Exercise 1: Output your favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
print("My favorite phone brand is:", x[1])  

# Exercise 2: Use negative indexing to print the 2nd last item
print("2nd last item:", x[-2])
 
 # Exercise 3: Update “iphone” to “itel”
# Tuples are immutable, so we must convert to list, change, then convert back
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print("Updated tuple:", x)

# Exercise 4: Add “Huawei” to your tuple
x = x + ("Huawei",)
print("Tuple after adding Huawei:", x)

# Exercise 5: Loop through the tuple
print("Looping through the tuple:")
for phone in x:
    print(phone)

# Exercise 6: Remove/delete the first item
x = x[1:]  # Skipping the first item
print("Tuple after removing first item:", x)

# Exercise 7: Create a tuple of cities using the tuple() constructor
cities = tuple(["Kampala", "Jinja", "Mbarara", "Gulu", "Arua"])
print("Ugandan cities tuple:", cities)

# Exercise 8: Unpack your tuple
city1, city2, city3, city4, city5 = cities
print("Unpacked cities:")
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)

# Exercise 9: Print the 2nd, 3rd, and 4th cities
print("2nd to 4th cities:", cities[1:4])

# Exercise 10: Join two tuples (first and second names)
first_names = ("Clerk", "Grace", "Paul")
second_names = ("Kats", "Kip", "Smith")
full_names = first_names + second_names
print("Joined names tuple:", full_names)

# Exercise 11: Create a tuple of colors and multiply it by 3
colors = ("red", "blue", "green")
colors_multiplied = colors * 3
print("Colors multiplied by 3:", colors_multiplied)
# Exercise 12: Count number of times 8 appears
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("Number of times 8 appears:", count_8)

#EXERCISE 3
# Exercise 1: Use set() constructor to create a set of 3 favorite beverages
beverages = set(["Tea", "Coffee", "Juice"])
print("Initial beverages set:", beverages)

# Exercise 2: Add 2 more items to the beverages set
beverages.update(["Water", "Soda"])
print("Updated beverages set:", beverages)

# Exercise 3: Check if "microwave" is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")

# Exercise 4: Remove "kettle" from the set
mySet.discard("kettle")  # Using discard avoids error if item doesn't exist
print("Set after removing 'kettle':", mySet)

# Exercise 5: Loop through the set
print("Looping through mySet:")
for item in mySet:
    print(item)

# Exercise 6: Add elements from a list to a set
my_set = {"pen", "pencil", "eraser", "ruler"}
my_list = ["marker", "sharpener"]
my_set.update(my_list)
print("Set after adding items from list:", my_set)

# Exercise 7: Join two sets: ages and first names
ages = {21, 25, 30}
first_names = {"Alice", "Brian", "Cathy"}
combined_set = ages.union(first_names)
print("Combined set of ages and names:", combined_set)

#EXERCISE 4
# Exercise 1: Declare an integer and a string and concatenate correctly
age = 25
message = "I am " + str(age) + " years old."
print(message)

# Exercise 2: Remove spaces at the beginning, in the middle, and at the end
txt = "      Hello,       Uganda!       "
clean_txt = " ".join(txt.split())  # Removes extra spaces and joins with single space
print("Cleaned text:", clean_txt)

# Exercise 3: Convert value of 'txt' to uppercase
uppercase_txt = txt.upper()
print("Uppercase text:", uppercase_txt)

# Exercise 4: Replace character 'U' with 'V'
replaced_txt = txt.replace('U', 'V')
print("Replaced text:", replaced_txt)

# Exercise 5: Return a range of characters in the 2nd, 3rd, and 4th positions
y = "I am proudly Ugandan"
range_chars = y[1:4]  # Index 1 to 3 (2nd to 4th characters)
print("Characters at 2nd to 4th positions:", range_chars)

# Exercise 6: Fix the string with internal quotes that causes an error
x = 'All "Software Engineers" are cool!'  # Use single quotes outside
print(x)

#EXERCISE 5
# Exercise 1: Define dictionary and print the value of the shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print("Shoe size:", Shoes["size"])

# Exercise 2: Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("Updated brand:", Shoes["brand"])

# Exercise 3: Add key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"
print("Added type:", Shoes)

# Exercise 4: Return a list of all the keys
keys = list(Shoes.keys())
print("Keys:", keys)

# Exercise 5: Return a list of all the values
values = list(Shoes.values())
print("Values:", values)

# Exercise 6: Check if key "size" exists
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")

# Exercise 7: Loop through the dictionary
print("Looping through dictionary:")
for key, value in Shoes.items():
    print(key, ":", value)

# Exercise 8: Remove "color" from the dictionary
Shoes.pop("color", None)  # `None` avoids error if key is not found
print("After removing color:", Shoes)

# Exercise 9: Empty the dictionary
Shoes.clear()
print("Dictionary after clearing:", Shoes)

# Exercise 10: Make a copy of another dictionary
my_profile = {
    "name": "Jane",
    "age": 22,
    "country": "Uganda"
}
profile_copy = my_profile.copy()
print("Original:", my_profile)
print("Copy:", profile_copy)

# Exercise 11: Show nested dictionaries
students = {
    "student1": {
        "name": "Alice",
        "age": 12
    },
    "student2": {
        "name": "Bob",
        "age": 13
    }
}
print("Nested dictionary:")
print(students)


