# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


def kind_of_triangle(num1, num2, num3):
  if (num1 == num2 and num2 == num3):
    return ("equalateral")
  elif (num1 == num2 or num2 == num3 or num1 == num3):
    return ("isosceles")
  else:
    return ("scalene")  

while True:
  print( "Enter the lengths of three side of a triangle:")
  side1=input("a: ")
  side2=input("b: ")
  side3=input("c: ")
  
  if side1.isalpha() or side2.isalpha() or side3.isalpha():
    print("Please only enter numbers. No letters.")
  else: 
    side1=int(side1)
    side2=int(side2)
    side3=int(side3)
    break

print(f"A triangle with sides of {side1}, {side2} & {side3} is a {kind_of_triangle(side1, side2, side3)}")