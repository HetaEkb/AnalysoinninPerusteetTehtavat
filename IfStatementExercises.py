# %%

# 1. 
number1 = 4
number2 = 6 

# a. 
if number1 == number2:
    print(str(number1) + " is equal to " + str(number2))
else:
    print(str(number1) + " is not equal to " + str(number2))

# b.
if number1 > number2:
    print(str(number1) + " is greater than " + str(number2))
else:
    print(str(number1) + " is not greater than " + str(number2))

# c. 
if number1 >= number2: 
   print(str(number1) + " is greater or equal to " + str(number2))
else:
    print(str(number1) + " is not greater or equal to " + str(number2))

# d.
if number1 != number2:
    print(str(number1) + " is not equal to " + str(number2))
else:
     print(str(number1) + " is equal to " + str(number2))


#2 
number1 = 1
number2 = 2
number3 = 3 

# a.
if number1 == number2 == number3:
    print("all numbers are equal")
else:
    print("not all numbers are equal")

# b. 
if (number1 == number2) or (number2 == number3):
    print(str(number1)) + "and" + (str(number2)) + "are equal or" + (str(number2)) + "and" + (str(number3) )
else:
    print("neither is true") 

# c.
if (number1 > number2) and (number1 > number3):
    print(str(number1)) + "is greater than" + (str(number2)) + "and" + (str(number1)) + "is greater than" + (str(number3) )
else:
    print("not true")

