print('if else elif ')
print(' ')

"""#if test_expression:
    # statement(s) to be run
##else:
   
   # statement(s) to be run
"""
a = 93
b = 27
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")

""" 
if test_expression:
    # statement(s) to be run
    if test_expression:
        # statement(s) to be run
    else: 
        # statement(s) to be run
elif test_expression:
    # statement(s) to be run
    if test_expression:
        # statement(s) to be run
    else: 
        # statement(s) to be run
else:
    # statement(s) to be run """


object_size=10
if object_size > 5:
    print("We need to keep an eye on this object")
else:
    print('Object poses no threat')

## AND / OR
"""  Toda la expresión de prueba se evalúa como True,
   porque se ha cumplido una de las condiciones de las subexpresiones """
print(' ')
print(' OR ')

a = 23
b = 34

if a == 34 or b == 34:
    print(a + b)

"""     toda la expresión de prueba se evalúa como False, 
porque solo una de las condiciones de las subexpresiones es true """
print(' ')
print('AND')
if a == 34 and b == 34:
    print (a + b)

object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')
    





