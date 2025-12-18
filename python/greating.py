import time

# Get the current time 
timestamp = time.strftime('%H:%M:%S')
print("Current Time:", timestamp)


hour, minute, sec = map(int, timestamp.split(':'))  # Convert all parts to integers

# Greating according to time
if 5 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 15:
    print("Good Afternoon!")
elif 15 <= hour < 19:
    print("Good Evening!")
else:
    print("Good Night!")


print("\n\n_______________________________________________________\n")
print("\t", sec % 7, sec % 9, sec % 5)
print("\t", sec % 8, sec % 3, sec % 6)
print("\t", sec % 3, sec % 7, sec % 9)