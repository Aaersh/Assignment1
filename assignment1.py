#************************************* QUESTION 1 *******************************************
# this is a program to find average of three numbers entered by the user
num1 = int(input("Enter the value of first number\n"))
num2 = int(input("Enter the value of second number\n"))
num3 = int(input("Enter the value of third number\n"))
avg = (num1+num2+num3)/3

print("The average of these three numbers is", avg)
#formula for average of three numbers a,b,c = (a+b+c)/3



#************************************* QUESTION 2 *******************************************
#this is a program to compute a person's income tax.
dependents = int(input("Enter the number of dependents\n"))
gross_income = float(input("Enter the gross income\n"))       #income is in dollars ($)

taxable_income = float(gross_income-10000-(3000*dependents))  #For each dependent, a taxpayer is allowed an additional $3,000 deduction.
income_tax = 0.2*taxable_income                               #All taxpayers are charged a flat tax rate of 20%.

print("Your net Income Tax is", income_tax)



#************************************** QUESTION 3 **********************************************
#this is a program to store different data type values into a list.
SID = int(input("Enter your SID\n"))
name = input("Enter your name\n")
gender = input("Enter your gender, Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown)\n")
course_name = input("Enter your course name\n")
CGPA = float(input("Enter your CGPA\n"))

student = [SID, name, gender, CGPA]
print(student)



#************************************* QUESTION 4 *********************************************
#this is a program to enter marks of 5 students into a list and display them in sorted manner.
student1 = int(input("Enter marks of first student\n"))
student2 = int(input("Enter marks of second student\n"))
student3 = int(input("Enter marks of third student\n"))
student4 = int(input("Enter marks of fourth student\n"))
student5 = int(input("Enter marks of fifth student\n"))

markslist = [student1, student2, student3, student4, student5]
markslist.sort()
print(markslist)



#************************************** QUESTION 5 **********************************************
color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
color.remove("Black")
print(color)

color1 = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
color1 = color1[:3] + ['Purple'] + color1[3+2:]   #index of 4th element is 3, performed slicing to replace black and pink with purple
print(color1)