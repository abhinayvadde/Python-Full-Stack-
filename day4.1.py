'''
# For printing the * in a hallow pyramidical view
n=int(input("Enter the required number of value:"))
for i in  range(1,n+1):
    if i==1 or i == n:
        print(" "*(n-i)+"* "*i)
    else:
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")
'''

'''
        1
       1 2
      1   3
     1     4
    1 2 3 4 5
'''
'''
n=int(input("Enter the required number of value:"))
for i in range(1,n+1):
    if i ==1 or i == n:
        str1 = ""
        for j in range(1,i+1):         #for printing the start and end values in the pattern
          str1 += str(j) + " "       # for 
        print(" "*(n-i)+str1)
    else:
        str2 = ""
        for k in range(1,i+1):
            if k == 1 or k == i:
              str2 += str(k) + " "
            else:
              str2 += " " + " "
        print(" "*(n-i)+str2)

'''
# This code is just to make the given series to a design model as per our requirement
n=int(input("Enter the required number of value:"))
for i in range(1,n+1):
    if i ==1 or i == n:
        str1 = ""
        for j in range(1,i+1):         
          str1 += str(j) + " "       
        print((" "*(n-i)+str1+" "*((n-i)*2)+str1+" "*((n-i)*2)+str1)*3)
    else:
        str2 = ""
        for k in range(1,i+1):
            if k == 1 or k == i:
              str2 += str(k) + " "
            else:
              str2 += " " + " "
        print((" "*(n-i)+str2+" "*((n-i)*2)+str2+" "*((n-i)*2)+str2)*3)


