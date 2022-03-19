import sys
sum = []
print('Бакалавариат ?')
a = input('Да/Нет\n')
if(a == 'Да'):
    sum.append(1)
else:
    sys.exit([0])
    
print('Аккредитация ?')
a = input('Да/Нет\n')
if(a == 'Да'):
    sum.append(1)
else:
    sum.append(0)
    
print('ВУЗ ?')
a = input('Да/Нет\n')
if(a == 'Да'):
    sum.append(1)
else:
    sum.append(0)
    
print('Оплата за год выше 100.000 ?')
a = input('Да/Нет\n')
if(a == 'Да'):
    sum.append(1)
else:
    sum.append(0)
    
print('Военная кафедра ?')
a = input('Да/Нет\n')
if(a == 'Да'):
    sum.append(1)
else:
    sum.append(0)
    
print('Бюджетных мест > 15 ?')
a = input('Да/Нет\n')
if(a == 'Да'):
    sum.append(1)
else:
    sum.append(0)
    
print('Проходной бал ?')
a = input('Да/Нет\n')
if(a == 'Да'):
    sum.append(1)
else:
    sum.append(0)
    
print('Общежитие ?')
a = input('Да/Нет\n')
if(a == 'Да'):
    sum.append(1)
else:
    sum.append(0)
count = 0
for i in (range(len(sum))):
    if(sum[i] == 1):
        count += 10;
    else:
        count +=0
print(count)