# -*- coding: utf-8 -*-
"""
@author: Zachary Wozich
Assignment 1
Class - Info 2820


For this assignment you will created a Python script that calculates the diameter, circumference, surface area, and volume of a sphere. Your script should conform to the following rules:
1. Please name your script <lastname>_sphere.py where <lastname> is your last name.
2. Take the radius of the sphere as input (as a floating-point number), after displaying an appropriate prompt.
3. Compute the sphere’s diameter, circumference, surface area, and volume. Use the following equations for reference.
diameter = 2 * radius
circumference = diameter * PI
surface area = 4 * PI * radius * radius
volume = 4/3 * PI * radius * radius * radius
4. Use the math module to get the value of PI for your calculations. Do not use a literal PI string of your own. That is, do not use something like pi = 3.14159.
5. Display the calculated diameter, circumference, surface area, and volume, each on a separate line and with appropriate text indicating what each value is. Each value should be rounded to 2 significant digits after the decimal place, using the round function.
As an example, when your script is run, it should take input and show output similar to the following (you can vary the text and formatting as you wish):
Enter the sphere's radius: 2.1
Diameter : 4.2
Circumference : 13.19
Surface area : 55.42
Volume : 38.79
When writing your script please remember to…
1. Add an appropriate docstring header to your program and any other appropriate comments in the source code.
2. Use well-named variables and an appropriate variable naming scheme. For example, if you use multi-word variables, either separate the words with underscores or use camelcase.
3. Test your program.
When you are done, please submit you script via the link provided in this week’s folder.
"""

#Use the math module to get the value of PI for your calculations

import math

#request radius a sphere from user

radius=float(input("Enter the sphere's radius: "))

#calculate the diameter of sphere

sphere_diameter = 2 * radius

#calculate the circumference of sphere

sphere_circumference = sphere_diameter * math.pi

#calculate the surface area of sphere

sphere_area = 4 * math.pi * pow(radius,2)

#calculate the volume of sphere

sphere_volume = (4/3) * math.pi * pow(radius,3)

#print output
print("")
print("Diameter      : %.2f" %sphere_diameter)
print("Circumference : %.2f" %sphere_circumference)
print("Surface area  : %.2f" %sphere_area)
print("Volume        : %.2f" %sphere_volume)
