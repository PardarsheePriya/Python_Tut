def greeting():
  print("Hello")


greeting()

#function that returns sum

def sums(a, b):
  return (a+b)

ans = sums(3, 9)
print(ans)

#function that returns difference

def diff(a, b):
  return(abs(a-b))

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Difference is: ")
print(diff(a, b))