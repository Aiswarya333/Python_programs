'''NAME THAT TRIANGLE - A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All 3 sides of an equilateral triangle
have the same length. An isosceles triangle has two sides that are the same length, and a third side that is a different length. If all of the sides have different
lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user. Display a message indicating the type of the triangle.'''

a=input("ENTER SIDE1 OF THE TRIANGLE  :")
b=input("ENTER SIDE2 OF THE TRIANGLE  :")
c=input("ENTER SIDE3 OF THE TRIANGLE  :")

if a==b==c:
        print("IT IS AN EQUILATERAL TRIANGLE")
elif a==b!=c or a==c!=b or b==c!=a:
        print("IT IS AN ISOSCELES TRIANGLE")
else:
    print("TRIANGLE IS SCALENE")
