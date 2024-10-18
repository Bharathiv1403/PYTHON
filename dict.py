students = [
    ("Alice", [85, 90, 92]),
    ("Bob", [78, 81, 85]),
    ("Charlie", [95, 87, 90])
]

# Create an empty dictionary to store the averages
student_avg = {}

# Loop through each student and calculate their average
for student in students:
    name, marks = student
    average = sum(marks) / len(marks)
    student_avg[name] = round(average, 2)

# Output the result
print(student_avg)
