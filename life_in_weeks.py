# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
final_age = 90 - age

days = 365 * final_age
weeks = 52 * final_age
months = 12 * final_age



print(f"You have {days} days, {weeks} weeks, and {months} months left.")
