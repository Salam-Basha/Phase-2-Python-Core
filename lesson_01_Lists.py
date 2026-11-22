# =========================================
# Lesson 01 — Lists
# =========================================

#Exercise 1 — Create a list

languages = ["Python" ,"Java", "JavaScript", "C"]
print(languages)


#Exercise 2 — Access element

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[-2])


#Exercise 3 — Modify a list

colors = ["Red", "Blue", "Green", "Yellow"]

colors[1] = "black"
colors[3] = "white"

print(colors)


#Exercise 4 — List length

games = ["mincraft" , "freefire" , "roblox" , "swordigo"]

print(games)
print(len(games))


#Exercise 5 — Membership

subjects = ["Maths", "Physics", "Chemistry", "Python"]

print("Python" in subjects)
print("Biology" in subjects)
print("Biology" not in  subjects)


#Challenge 🎯 — Student Information System

student = ["Salam", 18, "CSE", 85]

print(student[0])
print(student[1])
print(student[2])
print(student[3])

student[3] = 95

print(student)
print(len(student))

