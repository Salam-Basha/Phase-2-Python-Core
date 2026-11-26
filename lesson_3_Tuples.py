# ====================================
# Lesson 03: Tuples
# ====================================

#Create       -> a = (10, 20, 30)
#Single item  -> a = (10,)
#Indexing     -> a[0], a[-1]
#Slicing      -> a[0:2], a[::-1]
#Length       -> len(a)
#Membership   -> 10 in a
#Count        -> a.count(10)
#Index        -> a.index(20)
#Concatenate  -> a + (40, 50)
#Repeat       -> a * 2
#Unpacking    -> x, y, z = a


#Exercise 1: Create a tuple
#Create a tuple containing five programming languages and print it.

languages = ("python" , "C" ,"C++", "Java", "C#" )
print(languages)

#Exercise 2: Indexing

numbers = (10, 20, 30, 40, 50)

print(numbers [0])
print(numbers[2])
print(numbers[-1])

#Exercise 3: Slicing

print(numbers [0:3:1])
print(numbers[-1:-3:-1])
print(numbers[::-1])

#Exercise 4: Tuple methods

numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))
print(numbers.index(30))

#Exercise 5: Unpacking

student = ("Salam", 18, "CSE")

name, age, branch = student

print(name)
print(age)
print(branch)


#Challenge 🎯 — Student Record

student = ("salam",18,"CSE", "RGM")

print(student[0])
print(student[1])
print(student[2])
print(student[3])

print(len(student))

print("CSE" in student)

name, roll_no, branch, college = student

print(name)
print(roll_no)
print(branch)
print(college)
