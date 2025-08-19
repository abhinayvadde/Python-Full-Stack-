#Write a program that reads a two digit number N and check if any of the given conditions is satisfied 
# the number N is divisible by 9 and one of the digits of the number N is equal to 9 if any of the condition is satisfied then print lucky or else unlucky
'''
N = int(input("Enter the value:"))
if (N % 9 == 0 or '9' in str(N)):
    print("lucky number")
else:
    print("unlucky number")


N = input()
if(int(N)%9==0 or int(N[0])==9 or int(N[1])==9):
    print("lucky number")
else:
    print("unlucky number")
'''

# write a program that reads a distance D in km and calculates the total score : 
# for the first (0-40 km), the score for each km is 2.  
#for the next (41-60 km), the score for each km is 4.
# for the next (61-120 km), the score for each km is 6.
# for the distance above 120 km, the score for each km is 8.
# and add extra score of 50 points.
'''
D = int(input("Enter the values:"))
score =0
if ( 1 <= D <=40):
    score = (D*2)+50
elif (41 <= D <= 60):
        score = 130 + ((D-40)*4) 
elif (61 <= D <= 120):
        score = 210 + ((D-60)*6)
elif (D > 120):
        score = 570 + ((D-120)*8)
else:
       print("check correct input")
print(score)
'''

# write a program that reads two numbers X and N and prints the product of N numbers after X 
# Input: the first line of input contains an integer representing x and the second line of input contains an integer representing N.
# output: the output should be a single line containing an integer obtained by multiplying the N numbers after X
X = int(input("Enter the first value:"))
N = int(input("Enter the second value:"))
product = 1
for i in range(X + 1, X + N + 1):
    product *= i
print(product)






      
