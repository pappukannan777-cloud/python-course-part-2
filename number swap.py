a = int(input('enter a number'))

b = int(input('enter a number'))

c = int(input('enter a number'))

print("Before swapping:")
print(a, b, c)

a, b, c = b, c, a

print("After swapping:")
print(a, b,c)