student_scores = {
    "Billy": 81,
    "Jimmy": 78,
    "Timmy": 99,
    "Ram": 74,
    "Sam": 62,
}
#empty dicionary
student_grades = {}

# changes score into grades
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Eceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
print(student_grades)                