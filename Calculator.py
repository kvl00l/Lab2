#Kevin

#Calculator
def calculate(x1,x2,s1):
    if s1 == '+':
        result = x1+x2
    elif s1 == '-':
        result = x1-x2
    elif s1 == '*':
        result =  x1*x2
    elif s1 == '/':
        result = x1/x2
    elif s1 =='^':
        result =  x1**x2
    return result

# 1.Input
x1 = float(input("Type x1= "))
s1 = input('Enter operator (+,-,*,/,^): ') 
x2 = float(input("Type x2= "))

# 2.Process
sum= int(x1) + int(x2)

# 3. Output
result=calculate(x1,x2,s1)
print(x1,s1,x2)
print('=',result)
(f"Sum: {result}")