# Python code to demonstrate working
# of fabs() and abs()
import math

#################################
# When the argument is an integer#
################################# 
number = -10

# abs() will return an integer as
# the argument is an integer
print(abs(number))

# fabs() will return a floating point number
print(math.fabs(number))

###########################################
# When the input is a floating point number#
########################################### 
number = -12.08

# abs() will return an floating point number
# as the argument is a floating point number
print(abs(number))

# fabs() will return a floating point number
print(math.fabs(number))

####################################
# When the input is a complex number#
#################################### 
number = complex(3, 4)

# abs() will return the magnitude
print(abs(number))

# fabs() will return an error
# print(math.fabs(number))

