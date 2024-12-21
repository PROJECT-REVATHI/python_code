
try:
    even_numbers = [2,4,6,8,10]
    print(even_numbers[5])
except ZeroDivisionError:
    print("denominator cannot be zero")
except IndexError:
    print("array index out of bound")
