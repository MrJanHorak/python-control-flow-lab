# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

winter = ('dec', 'jan', 'feb', 'mar')
spring = ('mar', 'apr', 'may', 'jun')
summer = ('jun', 'jul', 'aug', 'sep')
fall = ('sep', 'oct', 'nov', 'dec')

def season(month, day):
  if month in winter:
    if month=='dec' and day>=21:
      return 'winter'
    elif month=='dec' and day<21:
      return "fall"
    elif month=='mar' and day<20:
      return "winter"
    elif month=='mar' and day>19:
      return "spring"
    else:
      return "winter"
  if month in spring:
    if month=="jun" and day<21:
      return "spring"
    elif month=="jun" and day>20:
      return "summer"
    else:
      return "summer"
  if month in summer:
    if month=="sep" and day<22:
      return "summer"
    if month=="sep" and day>21:
      return "fall"
    else:
      return "summer"
  if month in fall:
    return "fall"


while True:
  month=input("Enter a month of the year (Jan - Dec): ").lower()
  day=input("Enter the day of the month: ")
  if len(month)>3:
    print("Please enter the 3 letter abreviation for the month")
  elif int(day)>31:
    print("please enter a valid day of the month")
  elif month.isalpha and day.isnumeric():
    day=int(day)
    break
  else: 
    Print('Please make sure you only enter letters for the month and numbers for the day')

print(f"{month} {day} is {season(month,day)}")