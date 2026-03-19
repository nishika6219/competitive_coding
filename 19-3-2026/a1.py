#WAP to perform arithmatic function using functional programming approch

#pass #responsible to skip: bank acc use karo na karo par acc chalu krne ke liye min balance rakhna padhta h so same like this we can keep it empty

#functions help us to achive modularity approch and code reusability

import sys
def addition(num1,num2):
    print("addition : ", num1 + num2)
    
def substraction(num1,num2):#called function
    print("substraction : ", num1 - num2)
    

def multiplication(num1, num2):#called function
    print("multiplication : ", num1 * num2)
    

def division(num1,num2):#called function
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return
    print("division : ", num1 / num2)

while True:
    print("1. Addition")
    print("2. Substration")
    print("3. Multiplication")
    print("4. division")
    print("5. Exit")

    choice = int(input("Enter you choice from the above options: "))
    if choice == 5:
        sys.exit()

    val1 = int(input("Enter first value: "))
    val2 = int(input("Enter second value: "))
    
    if choice == 1:
        addition(val1, val2)
        #iske andr positional arugent pass krna hoga taki addition function dono value ko add krke result de sake
        
    elif choice == 2:
        substraction(val1, val2)      
    elif choice == 3:
        multiplication(val1, val2)
    elif choice == 4:
        division(val1, val2)
    else:
        print("Invalid choice. Please try again.")
