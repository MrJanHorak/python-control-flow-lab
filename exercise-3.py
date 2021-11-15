# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

def dog_years(num):
  if num<=2:
    num=num*10
  else:
    num=20+((num-2)*7)
  return (f"The dog's age in dog years is {num}")

while True:
  age=input("Input a dog's age in human years: ")

  if age.isalpha():
    print("Please only enter a number.")
  else:
    age=int(age)
    break

print(dog_years(age))