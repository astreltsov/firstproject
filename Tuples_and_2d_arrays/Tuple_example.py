my_tuple = ('green', 'red', 'blue')

joe_marks = [55, 63, 77, 81]
tom_marks = [65, 61, 67, 72]
beth_marks = [97, 95, 92, 88]

class_marks = [joe_marks, tom_marks, beth_marks]
print(class_marks)

for student_marks in class_marks:
    print(student_marks)

print(class_marks[0][2])