#impoting module by using import keyword using alias
#importing module
import numeric_calculation as nc

#-----------------------------------------------------
a = 5
b = 10
print("Sum of",a, "and",b,"is:", nc.calculate_addition(a,b))
#-----------------------------------------------------------
print("Difference of",a, "and",b,"is:", nc.calculate_difference(a,b))
#---------------------------------------------------
print("Multiplication of",a, "and",b,"is:", nc.calculate_multiplication(a,b))
#----------------------------------------------------------------------------
print("Divison of",a, "and",b,"is:", nc.calculate_division(a,b))
#------------------------------------------------------------------------
print("Modulus of",a, "and",b,"is:", nc.calculate_modulus(a,b))


'''Output:

Sum of 5 and 10 is: 15
Difference of 5 and 10 is: -5
Multiplication of 5 and 10 is: 50
Divison of 5 and 10 is: 0.5
Modulus of 5 and 10 is: 5

'''