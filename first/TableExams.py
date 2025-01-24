subjects = {}

while True:
    line = input("Enter pattern as Subject Surname Grade: ").strip()

    if not line:
        break

    subject, surname, grade = line.split()
    grade = int(grade)

    if subject not in subjects:
        subjects[subject] = {}

    if surname not in subjects[subject]:
        subjects[subject][surname] = []

    if grade not in subjects[subject][surname]:
        subjects[subject][surname].append(grade)

for subject, students in subjects.items():
    print(subject)
    for student, grades in students.items():
        print(f"{student} {' '.join(map(str, grades))}")
    print("-----")
