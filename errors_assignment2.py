#error handling
while True:
    try:
        
        num1 = float(input("Enter the first number: "))

     
        num2 = float(input("Enter the second number: "))

        
        result = num1 / num2

    except ValueError:
        print("input was invalid kindly enter numeric values.")
        continue  
    except ZeroDivisionError:
        print("Can't divide by zero. Please enter a non-zero second number.")
        continue  
    else:
        print(f"The result of {num1} / {num2} is {result}")
        break 
