try:
    age = int(input('Age: '))
    income = 2
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid Value')