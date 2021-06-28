print("Welcome to the Multipler 9000!")
print("For addition type +")
print("For subtraction type -")
print("For multiplication type *")
print("For division type /")
num1 = int(input("enter first value: "))
num2 = int(input("enter second value: "))

type = (input("enter type: "))
print(type)
if (type == "*" or type == "multiply"):
    print(num1, " *", num2)
    print((num1 * num2))
elif (type == "+" or type == "addition"):
    print(num1, " +", num2, "=")
    print((num1 + num2))
elif type == "-" or type == "subtraction":
    print(num1, "- ", num2, "= ", (num1 - num2))
elif (type == "/" or type == "division"):
    print(num1, "/", num2, "= ", (num1 / num2))
else:
    print("invalid")
