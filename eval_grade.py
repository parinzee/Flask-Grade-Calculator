def calculation(grade):
    grade = int(grade)
    grade = float(grade)

    if grade >= 93:
        calculation.grade = 4.0

    elif grade >= 90:
        calculation.grade = 3.7

    elif grade >= 87:
        calculation.grade = 3.3

    elif grade >= 83:
        calculation.grade = 3.0

    elif grade >= 80:
        calculation.grade = 2.7

    elif grade >= 77:
        calculation.grade = 2.3

    elif grade >= 73:
        calculation.grade = 2.0

    elif grade >= 70:
        calculation.grade = 1.7

    elif grade >= 67:
        calculation.grade = 1.3

    elif grade >= 63:
        calculation.grade = 1.0

    elif grade >= 60:
        calculation.grade = 0.7

    else:
        calculation.grade = 0


def calculation2(grade):
    grade = int(grade)
    grade = float(grade)

    if grade >= 93:
        calculation2.grade = 4.5

    elif grade >= 90:
        calculation2.grade = 4.2

    elif grade >= 87:
        calculation2.grade = 3.8

    elif grade >= 83:
        calculation2.grade = 3.5

    elif grade >= 80:
        calculation2.grade = 3.2

    elif grade >= 77:
        calculation2.grade = 2.8

    elif grade >= 73:
        calculation2.grade = 2.5

    elif grade >= 70:
        calculation2.grade = 2.2

    elif grade >= 67:
        calculation2.grade = 1.8

    elif grade >= 63:
        calculation2.grade = 1.5

    elif grade >= 60:
        calculation2.grade = 1.2

    else:
        calculation2.grade = 0