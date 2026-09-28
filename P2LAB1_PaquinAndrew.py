
#Andrew Paquin
#27 September 2026
#P2LAB1
#Performing mathematical calculations 

#import math module to use the constant, math.pi
import math 
#get radius from user
radius = float(input("Enter the radius of the circle: "))
print()
#calculate diameter
print("The diameter of the circle is:", 2 * radius)

#display diameter with 1 decimal point
print()
print("The diameter of the circle is: {:.1f}".format(2 * radius))

#calculate circumference
print()
print("The circumference of the circle is: {:.2f}".format(2 * math.pi * radius))

#calculate area
print()
print("The area of the circle is: {:.3f}".format(math.pi * radius ** 2))
