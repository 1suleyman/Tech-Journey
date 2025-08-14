print("Welcome to Grading Program! ")

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {

}
for x,y in student_scores.items():
    if y >= 91:
        student_grades[x] = "Outstanding"
    elif y >= 81:
        student_grades[x] = "Exceeds Expectations"
    elif y >= 71:
        student_grades[x] = "Acceptable"
    elif y <= 70:
        student_grades[x] = "Fail"

print(student_grades)
