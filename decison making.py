#weather = input("Enter the weather = ")
'''
if weather == "sunny":
    print("you can play outside")


print("have fun")'''
'''
if weather == "sunny":
    print("you can play outside")
else:
    print("Robot")

print("have fun")'''
'''
if weather == "sunny":
    print("you can play outside")
elif weather == "Rainy":
    print("Robot")
else:
    print("blocks")


print("have fun")'''


#calculator

num1 = int(input("Enter the number = "))
num2= int(input("Enter the number = "))
operator = input("Enter the operator = ")

if operator == "+":
    print(f"The sum two numbers {num1+num2}")
elif operator == "-":
    print(f"The sub two numbers {num1-num2}")
elif operator == "*":
    print(f"The mul two numbers {num1*num2}")
elif operator == "/":
    print(f"The div two numbers {num1/num2}")
else:
    print("Enter the oprator in +,-,*,/")