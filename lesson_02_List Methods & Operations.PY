# ========================================
# Lesson 02: List Methods & Operations
# ========================================

# append(x)          ->  Add one element at the end
# insert(i, x)       ->  Add element at a specific index
# extend(x)          ->  Add multiple elements
# remove(x)          ->  Remove by value
# pop(i)             ->  Remove by index (last element if no index)
# clear()            ->  Remove all elements
# sort()             ->  Sort ascending
# sort(reverse=True) -> Sort descending
# reverse()          ->  Reverse the list
# index(x)           ->  Find the index of an element
# count(x)           ->  Count occurrences
# copy()             ->  Create a shallow copy
# len(list)          ->  Count elements

# ==============================
# EXERCISES
# ==============================

# Exercise 1: append() and insert()

numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(1, 15)
print(numbers)

# Output: [10, 15, 20, 30, 40]


# Exercise 2: extend()

fruits = ["Apple", "Banana"]
fruits.extend(["Mango", "Orange"])
print(fruits)

# Output: ['Apple', 'Banana', 'Mango', 'Orange']


# Exercise 3: remove() and pop()

colors = ["Red", "Blue", "Green", "Yellow"]
colors.remove("Blue")
colors.pop()
print(colors)

# Output: ['Red', 'Green']


# Exercise 4: sort()

numbers = [45, 12, 89, 23, 5]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# Output:
# [5, 12, 23, 45, 89]
# [89, 45, 23, 12, 5]


# Exercise 5: count() and index()

numbers = [10, 20, 10, 30, 10, 40]

print(numbers.count(10))
print(numbers.index(30))

# Output:
# 3
# 3


# ==============================
# CHALLENGE: SHOPPING LIST
# ==============================

#Add "Rice" using append().
#Insert "Butter" at index 1.
#Remove "Eggs".
#Add "Apple" and "Mango" using extend().
#Sort the list alphabetically.
#Print the final shopping list.
#Print the total number of items.

s = ["Milk", "Bread", "Eggs"]

s.append("Rice")
print(s)

s.insert(1,"Butter")
print(s)

s.remove("Eggs")
print(s)

s.extend(["Apple","Mangoes"])
print(s)

s.sort()
print(s)

print(len(s))

# Output:
# ['Milk', 'Bread', 'Eggs', 'Rice']
# ['Milk', 'Butter', 'Bread', 'Eggs', 'Rice']
# ['Milk', 'Butter', 'Bread', 'Rice']
# ['Milk', 'Butter', 'Bread', 'Rice', 'Apple', 'Mangoes']
# ['Apple', 'Bread', 'Butter', 'Mangoes', 'Milk', 'Rice']
# 6


# ==============================
# COMMON MISTAKES
# ==============================

# append([1, 2]) adds one nested list.
# extend([1, 2]) adds two separate elements.

# remove("Apple") removes by value.
# pop(0) removes by index.

# sort() changes the original list.
# reverse() changes the original list.
# Both return None.

# index() raises ValueError if the element is missing.
# pop() raises IndexError if the index is invalid.


# =============================
# EXTRA EXAMPLE: copy()
# =============================

original = [10, 20, 30]
new_list = original.copy()

new_list.append(40)

print("Original:", original)
print("Copy:", new_list)

# Output:
# Original: [10, 20, 30]
# Copy: [10, 20, 30, 40]



