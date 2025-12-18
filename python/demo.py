# 1 
print("Hello python")
 
# 2
n1=input("Enter the first number:")
n2=input("Enter the second number:")
choice=input("Enter your choice (1: add) (2: sub) (3: mul) (4: div) (5: mod) (6: exp) (7: exit) ")
match choice:
    case '1':
        print("Addition:", int(n1) +int(n2))
    case '2':
        print("Subtraction:", int(n1) -int(n2))
    case '3':
        print("Multification:", int(n1) *int(n2))
    case '4':
        print("division:", int(n1) /int(n2))
    case '5':
        print("module:", int(n1) %int(n2))
    case '6':
        print("exponent:", int(n1) ^int(n2))
    case '7':
        exit()
    case _:
        print("Invalid choice.")
# 3
base=float(input("Enter the base: "))
height=float(input("Enter the height:"))
area = 0.5 * base* height
print("Area of tringle is:",area)
# 4
def cofficient(a,b,c):
    d = (b**2) - (4*a*c)
    if d > 0:  
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5 ) / (2*a)
        return (x1,x2)
    elif d == 0:
        x=(-b) / (2*a)
        return (x,x)
    else:
        x1=(-b - complex(0, d**0.5)) / (2*a)
        x2=(-b + complex(0, d**0.5)) / (2*a)
        return (x1,x2)

a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))
roots = cofficient(a,b,c)
print("Roots of the equation are:", roots)
# 5
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print("Before swapping: ",n1,n2)
n1=n1+n2
n2=n1-n2
n1=n1-n2
print("After swapping: ",n1,n2)
#6
def km_to_miles(kilometers):
    miles=float(kilometers*0.62137)
    return miles
km=float(input("Enter the distance in kilometers: "))
miles=km_to_miles(km)
print("{km} kilometers is equal to {miles} miles".format(km=km,miles=miles))
# 7
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius *1.8) + 32
    return fahrenheit
celsius = float(input("Enter the temperature in celsius"))
fahrenheit = celsius_to_fahrenheit(celsius)
print("{celsius} celsius is equal to {fahrenheit} fahrenheit".format(celsius=celsius,fahrenheit=fahrenheit))
# 8
num = float(input("Enter a number:"))
if num >0:
    print("the number is positive")
elif num<0:
    print("the number is negative")
else:
    print("the number is zero")

# 9
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 10
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
if leap_year(year):
    print("{year} is a leap year ".format(year=year))
else:
    print("{year} is not a leap year ".format(year=year))
# 11
def isprime(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if isprime(num):
    print("{num} is a prime number ".format(num=num))
else:
    print("{num} is not a prime number ".format(num=num))

    # 12
def print_all_primes(start,end):
    for num in range(start,end + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) ==0:
                    break
            else: 
                print(num,end=" ")
start = int(input("Enter the start of the range:"))
end = int(input("Enter the end of the range: "))
print("prime numbers between {start} and {end} are:".format(start=start,end=end))
print_all_primes(start,end)
# 13
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter a number to find its factorial: "))
result = factorial(n)
print("The factorial of {n} is {result}".format(n=n, result=result))
# 14
num = int(input("Enter a number: "))
print("Multiplication table of {num} is:".format(num=num))
for i in range(1,11):
    print("{num} X {i} = {result}". format(num=num,i =i, result=num*i)) 
15
def fibonacci(n):
    fib_sequence = []
    a, b = 0,1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b,a+b
    return fib_sequence

n=int(input("Enter the number of terms in the fibonacci sequence: "))
fib_sequence = fibonacci(n)
print("fibonacci sequence of {n} terms is:".format(n=n))
for num in fib_sequence:
    print(num, end= " ")
    print()

# 16
def armstrong_number(num):
    sum=0
    temp=num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum == num

num = int(input("Enter a number to check if it is an armstrong number: "))
if armstrong_number(num):
    print("{num} is an armstrong number".format(num=num))
else:
    print("{num} is not an armstrong number".format(num=num))
# 17
def armstrong_range(start,end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if armstrong_number(num):
            armstrong_numbers.append(num)
            return armstrong_numbers
        
start= int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
armstrong_numbers = armstrong_range(start,end)
print("Armstrong numbers between {start} and {end} are: ".format(start=start , end=end))
for num in armstrong_numbers:
    print(num, end=" ")
    print()

# 18
def find_sum_natural_numbers(n):
    if n < 0:
        return 0
    return n*(n+1)//2
n = int(input("Enter a natural number to find the sum of all natural numbers up to the given number: "))
result = find_sum_natural_numbers(n)
print("the sum of all natural numbers up to {n} is {result}".format(n=n,result=result))

# 19
def reverse_string(s):
    return s[::-1]
s= input("Enter a string to reverse it: ")
reversed_s = reverse_string(s)
print("the reversed string is : {reversed_s}".format(reversed_s=reversed_s))

# 20
