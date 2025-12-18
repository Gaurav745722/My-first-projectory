num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))

if num1==num2==num3:
    print("all equal.")   
# if num1 is greatest 
elif num1 > num2 and num1>num3:
       print(num1,"is greatest.")
# if num2 is greatest       
elif num2> num1 and num2>num3:
        print(num2,"is greatest.") 
# if num3 is greatest        
else :
    print(num3,"is greatest.")        
