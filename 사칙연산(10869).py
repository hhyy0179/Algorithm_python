import sys
input = sys.stdin.readline().rstrip()

num1,num2 = input.split()
num1 = int(num1)
num2 = int(num2)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)