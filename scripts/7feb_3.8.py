from random import randint
x = randint(1,50)
y = randint(2,5)
print('A random number between 1 and 50: ', x)
print('A random number between 1 and 50: ', y)
print(x ** y)

x = float(input ('voer de x in: '))
y = float(input ('voer de y in: '))
equation = float(abs(x-y)/(x+y))
print('x is: ', x)
print('y is: ', y)
print('the answer is: ', equation)
