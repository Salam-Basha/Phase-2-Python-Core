# =========================================
# Lesson 01 — Lists
# =========================================

# Create list:       numbers = [10, 20, 30]
# Empty list:        numbers = []
# First element:     numbers[0]
# Last element:      numbers[-1]
# Modify element:    numbers[1] = 50
# List length:       len(numbers)
# Check presence:    10 in numbers
# Check absence:     10 not in numbers

# IMPORTANT:
# - Lists use square brackets [].
# - Indexing starts from 0.
# - Lists are mutable (can be modified).
# - Lists allow duplicate and mixed data types.

# =========================================
# EXERCISES
# =========================================

# Exercise 1 — Create a list

languages = ["Python", "Java", "JavaScript", "C"]
print(languages)

# Exercise 2 — Access elements

numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[-2])

# Exercise 3 — Modify a list

colors = ["Red", "Blue", "Green", "Yellow"]
colors[1] = "Black"
colors[3] = "White"
print(colors)

# Exercise 4 — List length

games = ["Minecraft", "Free Fire", "Roblox", "Swordigo"]
print(games)
print(len(games))

# Exercise 5 — Membership

subjects = ["Maths", "Physics", "Chemistry", "Python"]
print("Python" in subjects)
print("Biology" in subjects)
print("Biology" not in subjects)


# CHALLENGE — STUDENT INFORMATION

student = ["Salam", 18, "CSE", 85]

print(student[0])
print(student[1])
print(student[2])
print(student[3])

student[3] = 95
print(student)
print(len(student))

# =========================================
# COMMON MISTAKES
# =========================================

# 1. Using {} instead of [].
# 2. Forgetting that indexing starts at 0.
# 3. Accessing an index that doesn't exist.
# 4. Confusing len() with the last index.
# 5. Trying to modify a string like a list.

# =========================================
# ANSWERS
# =========================================

# Exercise 1: 
# ['Python', 'Java', 'JavaScript', 'C']

# Exercise 2:
# 10, 30, 50, 40

# Exercise 3:
# ['Red', 'Black', 'Green', 'White']

# Exercise 4:
# 4

# Exercise 5:
# True, False, True

# Challenge:
# Salam, 18, CSE, 85
# ['Salam', 18, 'CSE', 95]
# 4
