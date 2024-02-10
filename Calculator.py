
print("Welcome to calculator!\n")

num1 = int(input("Enter number1:")) #Takes input of first number
num2 = int(input("Enter number2:")) #Takes input of second number

print("Enter your choice\n") #To take choices from the user
print("1.Addition\n")
print("2.Subtraction\n")
print("3.Multiplication\n")
print("4.Division\n")
ch = int(input("Enter your choice\n"))



if ch == 1:
 print("Addition is:",num1+num2) #Returns addition of two entered numbers.

elif ch == 2:
 print("Subtraction is:",num1-num2) #Returns Subtraction of two entered numbers.

elif ch == 3:
  print("Multiplication is:",num1*num2) #Returns Multiplication of two entered numbers.

elif ch == 4:
 print("Division is:",num1/num2) #Returns Division of two entered numbers.

else:
 print("Invalid choice!")
