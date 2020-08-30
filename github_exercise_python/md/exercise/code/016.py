import datetime

# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print(datetime.date.today().strftime('%d/%m/%Y'))

# 创建日期对象
birthDate = datetime.date(1941, 1, 5)

print(birthDate.strftime('%d/%m/%Y'))

# 日期算术运算
birthNextDay = birthDate + datetime.timedelta(days=1)

print(birthNextDay.strftime('%d/%m/%Y'))

# 日期替换
firstBirthday = birthDate.replace(year=birthDate.year + 1)

print(firstBirthday.strftime('%d/%m/%Y'))
