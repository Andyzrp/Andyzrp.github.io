N = 3
student = []
for i in range(5):
    student.append(['', '', []])


def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:')
        stu[i][1] = input('input student name:')
        for j in range(3):
            stu[i][2].append(int(input('score:')))


def output_stu(stu):
    for i in range(N):
        print(f'{stu[i][0]}\t{stu[i][1]}')
        for j in range(3):
            print(f'{stu[i][2][j]}', end="\t")
        print()


input_stu(student)
print(student)
output_stu(student)
