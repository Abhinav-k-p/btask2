def operations():
    a=int(input('enter the first number'))
    b=int(input('enter the second number'))
    sum=a+b
    sub=a-b
    mul=a*b
    return sum,sub,mul
print(operations())

def operations1(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    return sum,sub,mul
x=int(input('enter the first number'))
y=int(input('enter the second number'))
print(operations1(x,y))

def perform_operations3(a, b):
      print("Sum:", a + b)
      print("Subtraction:", a - b)
      print("Multiplication:", a * b)
x=int(input('enter the first number'))
y=int(input('enter the second number'))
perform_operations3(x,y)


def perform_operations4():
    a = x
    b = y
    print("Sum:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
x=int(input('enter a number: '))
y=int(input('enter a number: '))
perform_operations4()