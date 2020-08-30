score = int(input('输入分数:'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print(f'{score} 属于 {grade}')
