# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.


# sums = lambda a: a + 15
# print(sums(5))
#
# mul = lambda x, y: x * y
# print(mul(5, 10))


# 2.  Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

# def UnknownMul(n):
#     return lambda x: x * n
#
#
# result = UnknownMul(5)
# for i in range(1,11):
#     print(result(i))


# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


# LoT = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# LoT.sort(key = lambda x : x[1])
# print(LoT)

# a = [1,2,3,4,5]
# result = list(map(lambda x:x**3,a))
# print(result)


# 4. Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#  {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#  {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

# a = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#      {'make': 'Samsung', 'model': 2, 'color': 'Blue'}]
# result = sorted(a, key=lambda x: x['model'])
# print(result)


# 5. Write a Python program to filter a list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = list(filter(lambda x: x % 2 == 0, a))
# c = list(filter(lambda x: x % 2 != 0, a))
# print(f"Even: {b}\nOdd: {c}")


# 6. Write a Python program to square and cube every number in a given list of integers using Lambda.
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = list(map(lambda x: x ** 2, a))
# c = list(map(lambda x: x ** 3, a))
# print(f"Square: {b}\nCube: {c}")


# 7. Write a Python program to find if a given string starts with a given character using Lambda.
# GivenString = "Abra Ka Dabra"
# result = lambda x: True if GivenString.startswith('a') else False
# print(result(GivenString))


# 8. Write a Python program to extract year, month, date and time using Lambda.
# s = "2020-01-15 09:03:32.744178"
# DateTime = s.split(" ")
# Time = DateTime[1].split(":")
# Date = DateTime[0].split("-")
# DateName = ['Year', 'Month', 'Date']
# TimeName = ['Hours', 'Minutes', 'Second']
# DateGiven = dict(zip(DateName, Date))
# TimeGiven = dict(zip(TimeName, Time))
# DateGiven.update(TimeGiven)
# print(DateGiven)


# 9. Write a Python program to check whether a given string is number or not using Lambda.
# Num = lambda x : True if x.isnumeric() else False
# print(Num('336'))


# dig = 4
# num = 9
# result = 0
# for i in range(1,dig+1):
#     result += int(str(num)*i)
#     print((str(num)*i))
# print(result)