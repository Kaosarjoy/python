#python index.py
a= int(input('Enter the first number'))
b = int(input('Enter the second number'))
c = int(input('Enter the third number'))
sum = a + b + c
#print("the sum is ", sum)
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if (a > b) and (a > c):
    print("The biggest number is", a)
elif (b > a) and (b > c):
    print("The biggest number is", b)
else:
    print("The biggest number is", c)

# for loop 
for i in range(10, 0, -1):  
    print(i)

for i in range(1, 11):  
    print(i)
