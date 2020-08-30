def varfunc():
    var = 0
    print(f'var = {var}')
    var += 1


for i in range(3):
    varfunc()


# 类的属性
# 作为类的一个属性吧
class Static(object):
    StaticVar = 5

    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)


print(Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()
