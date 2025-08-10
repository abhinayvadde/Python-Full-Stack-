# For printing prime numbers between two values range we use this code
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

m = int(input("Enter the first value:"))
n = int(input("Enter the second value:"))
if m >n:
    print("please enter the correct range")
elif (m<0 and n<=0):
    print("No prime numbers in this range")
else:
    for i in range(1, m + 1):
     is_prime(i)

#Addition using functions
def add(x,y):
   return(x+y)

a = int(input('Enter the first value:'))
b= int(input('Enter the second value:'))

c= add(a,b)
print('The output of the sum is',c)



def greet(arg_1 = "Hi!",arg_2 = "Ram"):
   print(arg_1+" " + arg_2)

greeting = input()
name = ()
greet(arg_1= greeting , arg_2 = name)

# to print factorial numbers using recursion method
def  fact(n):
    if n ==1:           # here we can use other condition as if we enter the value as 0 then error occurs so to eleminate this we use another condition
        return 1        # that is n<=0
    return n*fact(n-1)

n= int(input("Enter the values: "))
print(fact(n))


# to print the sum of first n natural numbers using recursion
def  fact(n):
    if n ==1:           
        return 1      
    return n+fact(n-1)

n= int(input("Enter the values: "))
print(fact(n))


# for printing of fibonnoci series using recursion but it is tame taking process as the execution takes more time 
# it is also known as tabulation method which consumes more space and it is dynamic
def fibb(n):
    if n <=0:
        return 0
    if n == 1:
        return 1
    return fibb(n-1)+fibb(n-2)
n = int(input('enter the value:'))
for i in range(n):
    print(fibb(i))

# This is an example for the set data type in python
# It is unordered and unindexed collection of items
a =2 
set_a ={5 ,"six",a,8.2}
set_a.add("mukesh") # This will raise an error as add() method can take only one argument
print(type(set_a))
print(set_a)


# Dictionary is a collection of key-value pairs and it is unordered, changeable, and indexed.
dict_a = {
    "name": "mukesh",
    "age": 20,
    "marks": [90, 80, 70],
    "is_student": True
}
print(type(dict_a))
print(dict_a)

# Examples for oops concepts in python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an instance of the Student class
kp = Student("Mukesh", 20)
kp.display()



class Iphone:
    def icloud(self):
        print("free 5gb space")

    def call(self,number):
        print(f"Calling {number} from iPhone")

iphone16pro = Iphone()

no = int(input("Enter the number to call: "))
print(type(iphone16pro))
iphone16pro.call(no)


class student:
    def __init__(self, name, rollno, branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        print("constructor called")

    def __del__(self):
        print("Destructor called")
              
    s1 = student("Mukesh", 123, "CSE")
    s2 = student("Ram", 456, "ECE")
    


class Amazonwebservices:
    def __init__(self, name , agentid , customerid):
        self.name = name
        self.agentid = agentid
        self.customerid = customerid 

customer = int(input("Enter the customer id: "))
agentid = int(input("Enter the agent id: "))
agentname = input("Enter the agent name: ")

agent1 = Amazonwebservices(agentname, agentid, customer)
print(f"Agent Name: {agent1.name}, Agent ID: {agent1.agentid}, Customer ID: {agent1.customerid}")



class AmazonService:
    def __init__(self, name, agentId, custId):
        self.name = name
        self.agentId = agentId
        self.custId = custId

agentName = 'sai'
AgentId = 1

complaint = input("Enter your issue:")
customerId = int(input("Enter your customer id: "))
while complaint:
    agent1 = AmazonService(agentName,AgentId,customerId)
    complaint = False
print("agent",agent1.agentId, "is handling customer", agent1.custId)



