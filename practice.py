# #take input as list and then add them

# num = input("Enter the numbers : ").split()

# num = [int(i) for i in num]

# # sum = 0
# # for i in num:
# #     sum += i

# total = sum(num)
# print(total)

# # use python's inbuit sum method


#calculator
a = int(input("first number : "))
op = input("Enter the operation you want to perform : ")
b = int(input("second number : "))

if op == '+':
    print(a + b, " - Sum of a & b")
elif op == '-':
    print(a - b, " - Diff of a & b")
elif op == '*':
    print(a * b, "- product of a & b")
elif op == '/':
    print(a / b, "- quotient of a & b")
else:
    print("Invalid operation")







