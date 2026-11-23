# ==============================================
# Lesson 02 — List Methods & Operations
# ==============================================


# append(x)	     Add one element at the end
# insert(i, x)	 Add at a specific index
# extend(list)	 Add multiple elements
# remove(x)	     Remove by value
# pop(i)	     Remove by index
# clear()	     Remove everything
# sort()	     Sort elements
# reverse()	     Reverse current order
# index(x)	     Find element position
# count(x)	     Count occurrences
# copy()	     Create a shallow copy


# Exercise 1 — Append and Insert

numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(1,15)
print(numbers)

# Exercise 2 — Extend

fruits = ["Apple", "Banana"]
fruits.extend(["mango","orange"])

print(fruits)

# Exercise 3 — Remove

colors = ["Red", "Blue", "Green", "Yellow"]
colors.remove("Blue")
colors.pop(2)

print(colors)

# Exercise 4 — Sorting

numbers = [45, 12, 89, 23, 5]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# Exercise 5 — Count and Index

numbers = [10, 20, 10, 30, 10, 40]

print(numbers.count(10))
print(numbers.index(30))

# Challenge 🎯 — Shopping List Manager

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

