# import random
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# n =3
# password = ""
# while(n==0):
#      for i in range(1,  n + 1): 
#        for j in range (1):
#         char = str(random.choice(numbers))
#         password = password + char
       
#      print(" "+password)
    
# n=n-1

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("500x300")

# Add a label
label = tk.Label(root, text="What's your next step !")
label.pack(pady=10)

# Add a button
def say_hello():
    label.config(text="Hello Everyone! ")

def militry():
    label.config(text="Welcome to US Militry ")


def calculator():
     n1=int(input("Enter first number: "))
     n2=int(input("Enter second number: "))
     

     # chose operator
     operator = input("chose operator: ")

     match operator:
      case "+": 
        print("Sum is ",n1+n2)
      case "-": 
        print("Difference is ",n1-n2)
      case "*": 
        print("Product is ",n1*n2)
      case "**": 
        print("Double Product is ",n1**n2)    
      case "/": 
        print("Division is ",float(n1/n2))
      case "//":
        print("Double Division is ",n1//n2)
      case "%": 
        print("Modulas first of second  is ",n1 % n2)
      case "_":
        print("invalid operator you chosed")
    

button = tk.Button(root, text="Gretting", command=say_hello)
button.pack(pady=10)

button = tk.Button(root, text="Calculator", command=calculator)
button.pack(pady=10)

button = tk.Button(root, text="Militry system", command=militry)
button.pack(pady=10)

# Start the GUI loop
root.mainloop()

