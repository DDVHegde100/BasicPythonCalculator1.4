# define functions  
def add(x, y):  
   """This function adds two numbers!"""
   return x + y 
def subtract(x, y): 
   """This function subtracts two numbers!""" 
   return x - y 
def multiply(x, y): 
   """This function multiplies two numbers!""" 
   return x * y 
def divide(x, y): 
   """This function divides two numbers!"""  
   return x / y 
def sqrt(x)
   """This function finds the root of the value!"""
# take input from the user  
    print("Select operation.")  
    print("1.Addition")  
    print("2.Subtraction")  
    print("3.Multiplication")  
    print("4.Division")  
    print("5.Square Root")
  
choice = input("Enter operation value(1,2,3,4,5):")  
    num1 = int(input("Enter first value: "))  
    num2 = int(input("Enter second value: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2)) 
elif choice == '5':  
   print(num1, sqrt(num1)) 
else:  
   print("Invalid input. Please enter a proper operation value")  