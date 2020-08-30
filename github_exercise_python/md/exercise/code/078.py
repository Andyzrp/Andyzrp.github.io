person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
m = 'li'
for key in person.keys():
    if person[m] < person[key]:
        m = key

print(f'{m}\t{person[m]}')
