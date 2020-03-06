def exponentiate(x:int,y:int):
    return x**y
print (exponentiate(2,2))

def raise_to_fourth_power(x:int):
    return exponentiate(x,4)
print (raise_to_fourth_power(2))


square = lambda x: exponentiate(x, 2)
print (square(2))

cube = lambda x: exponentiate(x, 3)
print (cube(2))
