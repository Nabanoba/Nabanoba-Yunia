import datetime
print("Script started at:", datetime.datetime.now())
# Exercise 1: Create a list with 5 items (names of people) and output the 2nd item
print("=== Exercise 1 ===")
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("2nd item:", people[1])

# Exercise 2: Change the value of the first item to a new value
print("\n=== Exercise 2 ===")
people[0] = "Alex"
print("Updated list:", people)

# Exercise 3: Add a sixth item to the list
print("\n=== Exercise 3 ===")
people.append("Frank")
print("After adding 6th item:", people)

# Exercise 4: Add "Faith" as the 3rd item
print("\n=== Exercise 4 ===")
people.insert(2, "Faith")
print("After inserting 'Faith' as 3rd item:", people)

# Exercise 5: Remove the 4th item from the list
print("\n=== Exercise 5 ===")
del people[3]
print("After removing 4th item:", people)

# Exercise 6: Use negative indexing to print the last item
print("\n=== Exercise 6 ===")
print("Last item:", people[-1])

# Exercise 7: Create a full list with 7 items and print 3rd, 4th, and 5th items
print("\n=== Exercise 7 ===")
items = ["A", "B", "C", "D", "E", "F", "G"]
print("3rd to 5th items:", items[2:5])

# Exercise 8: List of countries and make a copy of it
print("\n=== Exercise 8 ===")
countries = ["Kenya", "Uganda", "Tanzania", "Rwanda"]
countries_copy = countries.copy()
print("Original list:", countries)
print("Copied list:", countries_copy)

# Exercise 9: Loop through the list of countries
print("\n=== Exercise 9 ===")
print("Looping through countries:")
for country in countries:
    print("-", country)

# Exercise 10: List of animal names and sort them
print("\n=== Exercise 10 ===")
animals = ["zebra", "lion", "elephant", "giraffe", "monkey"]
ascending = sorted(animals)
descending = sorted(animals, reverse=True)
print("Animals ascending:", ascending)
print("Animals descending:", descending)

# Exercise 11: Output only animals with the letter 'a'
print("\n=== Exercise 11 ===")
a_animals = [animal for animal in animals if 'a' in animal]
print("Animals with 'a':", a_animals)

# Exercise 12: Join two lists of first and second names
print("\n=== Exercise 12 ===")
first_names = ["John", "Jane", "James"]
second_names = ["Doe", "Smith", "Brown"]
joined_names = first_names + second_names
print("Joined names:", joined_names)
