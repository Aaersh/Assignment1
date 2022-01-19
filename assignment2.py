#****************************************** QUESTION 1 ***********************************************

inputstring = "Python is a case sensitive language."
print(len(inputstring))                                             #to Find the length of the input string.
print(inputstring[::-1])                                            #to Reverse the order of the string
newstring = inputstring[10:26]                                      #to store “a case sensitive” in new string.
print(newstring)
print(inputstring.replace("a case sensitive", "object oriented"))   #to Replace “a case sensitive” with “object oriented”.
print(inputstring.index("a"))                                       #to Find index of substring “a” in the given input string.
print(inputstring.replace(" ", ""))                                 #to Remove the white spaces from the given input string.









#****************************************** QUESTION 2 ***********************************************

name = "Aaersh Kumar"
sid = "21103037"
department = "Computer Science and Engineering"
cgpa = "9.9"
print("Hey,",name, "Here!\nMy SID is", sid, "\nI am from",department, "department and my CGPA is",cgpa)








#****************************************** QUESTION 3 *********************************************

a = 56
b = 10
print(a&b)
print(a|b)
print(a^b)
print(a<<2, b<<2)
print(a>>2, b>>4)








#****************************************** QUESTION 4 *********************************************
#this is a program to find the greatest of three numbers entered by the user.

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))
num3 = int(input("Enter third number\n"))

if num1>num2:
    if num1>num3:
        print("the greatest of three numbers is", num1)
    else:
        print("the greatest of three numbers is", num3)

else:
    if num2>num3:
        print("the greatest of three numbers is", num2)
    else:
        print("the greatest of three numbers is", num3)








#****************************************** QUESTION 5 ***************************************

user_string = str(input("Enter the string\n"))
index = user_string.find(" name ")
if index==-1:
    print("No, the word “name” is not present in the string.")
else:
    print("Yes, the word “name” is present in the string.")








#****************************************** QUESTION 6 *********************************************
#this is a program to check whether the given input lengths can form a triangle or not.

a = int(input("Enter length of first side\n"))
b = int(input("Enter length of second side\n"))
c = int(input("Enter length of third side\n"))

if a+b>=c and b+c>=a and a+c>=b:                       #If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle.
    print("Yes, triangle can be formed.")

else:
    print("No, triangle cannot be formed.")
