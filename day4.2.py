'''
#Named Arguments
def greet(arg1,arg2):
    print("Hello",arg1,"i am",arg2,"years old !")

name = input()
age = int(input())
greet(arg2 = age, arg1 = name)

# check wether the given number is amstrong or not
#Method -1
given_number = input("Enter the required value:")
given_number = str(given_number)
string_length = len(given_number)
sum = 0
for i in given_number:
    sum += int(i)**string_length
if sum == int(given_number):
    print("The given number",given_number,"is an Amstrong number.")
else:
    print("The given number",given_number,"is not an Amstrong number.")

#Method-2
n = str(input())
s = 0
power = len(n)
for i in n:
    s += int(i)** power
if s == int(n):
    print("given is amstrong")
else:
    print("is not amstrong")


p = int(input("Enter the value:"))
count = True
for i in range(2,p+1):
    for j in range(1,i+1):
        if i%j != 0:
            count += str(p)
        else:
            m += str(p)
print(count)
'''


def is_prime(m):
    is_prime = True
    if m <=1:
        is_prime = False
    else:
        for i in range(2, int(m**0.5) + 1):
            if m % i == 0:
                is_prime = False
                break
    if is_prime:
        print(m, "is a prime number.")

m = int(input("Enter the value:"))
for i in range(1, m + 1):
    is_prime(i)