#arthemetic operations
salary=25000
ha=salary*0.20
dfa=salary*0.10
total_salary = salary + ha + dfa
print("total salary;", total_salary)

a = 10
b = 3

print("addition:", a + b)
print("subraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("floor division:", a // b)
print("remainder:", a % b)
print("power:", a ** b)

#simple calculator 
a = int(input("Enter first number"))
b = int(input("Enter second number"))

print("addition:", a + b)
print("subraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#student marks caluculator
name = input("Enter student name; ")

m1 = int(input("Enter python marks; "))
m2 = int(input("Enter java marks; "))
m3 = int(input("Enter sQL marks; "))

total = m1 + m2 + m3
average = total / 3

print("\n----- student Report -----")
print("Name;", name)
print("Total;" , total) 

#shopping bill caluculator
price1= float(input("Enter product 1 price: "))
price2 = float(input("Enter product 2 price: "))
price3 = float(input("Enter product 3 price: "))

total = price1 + price2 + price3 

discount = total * 0.10
final_amount = total - discount
print("Discount;", discount)

#comparison operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >=b)
print(a <=b)

#age eligibility checker
age = int(input("Enter you age; "))

print("Eligible;", age >= 18)

#pass or fail checker
marks = int(input("Enter marks: "))

print("passed:", marks >= 40)
#login validation
correct_username = "admin"15

correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

print(username == correct_username)
print(password == correct_password)

#assignment operators
x = 10

x += 5
print(x)

x -= 2
print(x) 

x *= 3
print(x)

#bank balance
balance = 10000

deposit = 5000
balance += deposit
print("after Deposit;", balance)

withdraw = 2000
balance -= withdraw
print("After withdrwal;", balance)


#atm eligibilty checker
balance = 10000
withdraw = 5000

print(withdraw > 0 and withdraw <= balance)