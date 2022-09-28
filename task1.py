day = int(input('Enter day number: '))
if day > 7 or day < 1:
     print("Повторите ввод от 1 до 7")
elif day == 6 or day == 7:
     print("Выходной")
else:
     print("Этот день не выходной")