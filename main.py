#WRITE YOUR CODE IN THIS FILE
def factorial(x):
    y = 1
    z = 1
    for i in range(0, x):
       y = y * z
       z = z + 1
    return y

print(factorial(5))