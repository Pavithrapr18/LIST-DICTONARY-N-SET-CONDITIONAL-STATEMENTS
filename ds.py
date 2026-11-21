# 1 List creation
age_list = [24, 25, 26, 27, 28]
print("Age List:", age_list)


name_list = ["Anu", "Meera", "Ravi", "Kiran", "Divya"]
print("Name List:", name_list)


# 2 List operation
name_list.append("Yazhini")
print("After Append:", name_list)


age_list.insert(2, 30)
print("After Insert:", age_list)


name_list.remove("Yazhini")
print("After Remove:", name_list)


age_list.pop()
print("After Pop:", age_list)


age_list.extend([29, 30, 26])
print("After Extend:", age_list)


age_list.sort(reverse=True)
print("Descending Order:", age_list)


print("Maximum Age:", max(age_list))
print("Minimum Age:", min(age_list))
print("Sum of Ages:", sum(age_list))


# 3. Accessing List Elements
print("First Name:", name_list[0])


print("Last Name:", name_list[-1])


print("Index 2 to 4:", name_list[2:5])


print("Reverse List:", name_list[::-1])


# Dictionary

student_marks = {
    "Anu": 85,
    "Ravi": 90,
    "Meera": 78,
    "Arjun": 88,
    "Kiran": 75
}

print("Student Marks:", student_marks)


print("Ravi's Mark:", student_marks["Ravi"])


student_marks["Janani"] = 80
print("After Adding Janani:", student_marks)


student_marks["Anu"] = 82
print("After Updating:", student_marks)


print("Student Names:", student_marks.keys())

print("Marks:", student_marks.values())

print("Student Details:", student_marks.items())

# Sets

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print("My Set:", my_set)


try:
    my_set[4] = 's'
except TypeError as e:
    print("Error:", e)


set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}


print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))



# Operators and conditional statements

score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score! Enter a score between 0 and 10.")

elif score > 7:
    print("Above Average: Excellent performance! Keep it up.")

elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")