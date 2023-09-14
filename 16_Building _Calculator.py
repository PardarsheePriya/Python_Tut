num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

op = input("Enter Operator: ")

if(op == '+'):
  print(num1 + num2)

elif(op == '-'):
  print(abs(num1-num2))

elif(op == '*'):
  print(num2*num1)

elif(op == '/'):
  print(num1/num2)
else:
  print("Invalid Operator")