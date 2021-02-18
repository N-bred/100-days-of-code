print("Welcome to  the bill calculator")

price = float(input("What was the total bill? $"))

percentage = float(input("What percentage tip would you like to give? "))

n_of_people = float(input("How many people to split the bill? "))

total = price + (price * percentage / 100)

each_pay = total / n_of_people

print(f"Total bill: ${total}")

print(f"Each person should pay: ${round(each_pay, 2)}")