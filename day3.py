#finding out the unique numbers
list_1 = [1,2,3,4,5,5,4,3,2,1,7]
first_sum = sum(list_1)
second_sum = sum(set(list_1))*2
res = second_sum-first_sum
print(res)


#finding of the factorial of a number given
n = int(input("Enter the input :"))
fact = 1
for i in range(n,0,-1)
    fact = fact*i
print(fact)


# printing of the multiples sum until requried value of multiple
n = int(input("Enter the value="))
f = 0
m = int(input("enter the range:"))
for i in range(1,m,1):
   f = n*i + f
   print(n,"*",i,"=",f)
print(f)


#for finding out the required value from a list of values given
# Note: here if a number is present in multiple times then only first  index value of that number is printed 
values=[1,2,3,6,9,8,5,4,3,6]
required = int(input("Enter the required value:"))
for i in range(len(values)):
    if required == values[i]:
        print(i)
        break

#for finding out the required value from a list of values given
# Note: here if a number is present in multiple times then all the index value of that number is printed 
values=[1,2,3,6,9,8,5,4,3,6]
required = int(input("Enter the required value:"))
for i in range(len(values)):
    if required == values[i]:
        print(i)


# Program for printing the index of a value with less number of iteration count
list_1 = [1,2,3,4,5,6,7,8,9,10]
target =11
start = 0
end = len(list_1)-1
index = -1
while(start<=end):
    middle = (start+end)//2
    if list_1[middle]==target:
        index = (middle)
        break
    elif list_1[middle]>target:
        end = middle-1
    elif list_1[middle]<target:
        start = middle+1 
print(index)
print("index of value is",middle)

input=[1,2,3,9,8,7,56]
r = 0
for i in range(len(input)):
    if input[i] > r:
        r = i
print(r)

# for printing the stars in right angle triangle
n=int(input("Enter the required number of value:"))
for i in range(1,n+1):
    print("* "*i)

# for printing the stars in reverse(inverted) right angle triangle
n=int(input("Enter the required number of value:"))
for i in range(n,0,-1):
    print("* "*i)


#for printing the numbers in order 
n=int(input("Enter the required number of value:"))
for i in range(1,n+1):
   str_1 = " "
   for j in range(1,i+1):
      str_1 += str(j)+" "
   print(str_1)

#for printing the numbers in reverse order with descending values
n=int(input("Enter the required number of value:"))
for i in range(n,0,-1):
   str_1 = " "
   for j in range(i,0,-1):
      str_1 += str(j)+" "
   print(str_1)



#waste dumb for my sake
n=int(input("Enter the required number of value:"))
for i in range(1,n+1):
    print(" "*i,"* "*i,""*i,"* "*i)

    

#for printing stars in pyramid form with simple steps in top to bottom
n=int(input("Enter the required number of value:"))
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)

    
#for printing stars in pyramid form with simple steps in bottom to top reverse order
n=int(input("Enter the required number of value:"))
for i in range(n,0,-1):
    print(" "*(n-i),"* "*i)



# for printing the stars with hallow structure
n=int(input("Enter the required number of value:"))
for i in  range(1,n+1):
    if i==1 or i == n:
        print("* "*i)
    else:
        print("*"+" "*(2*i-3)+"*")


n=int(input("Enter the required number of value:"))
for i in  range(1,n+1):
    if i==1 or i == n:
        print(" "*(2*i-3) +"* "*i)
    else:
        i = i+i
        print("*"+" "*(i) + "*")