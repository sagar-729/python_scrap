try:
    a = 20
    b = 0
    print(a / b)
except ZeroDivisionError:
    print('There is divide by zero error')
finally:
    print("this is going to print , no matter what.")