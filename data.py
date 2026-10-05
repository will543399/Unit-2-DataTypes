'''

x=6
y=float(3)
print(x,y)


bill= int(input("how much was the bill"))
tip=float(input("How much do you want to tip for the service"))
print(bill + (bill*tip))

values=[1,2,23,5,7,2,30,15]
print(values) 
for i in values:
    print(i)
x="this is a thing"
y=x.split( )
z=y[0]
print(y)
print(z)


answer=input("give me a random sentence")
y=len(answer.split( ))


print(y)




dayoftheweek=input("what day of the week is it?")
if dayoftheweek=="Friday":
    print ("Correct")
else:
    print("Incorrect") 
students= ["Ellie","Ben","Preston"]
students.append("Sofia") 
print(students[-1])
#gets the last of the list

for student in students:
    if student=="Ben":
        print(f'we found{student}')

x="test"
print(f"hello{x}")
temp=75
if temp>68:
    print("warm")
elif temp==68:
    print("Perfect")
else:
    print("cold")

#the user will imput a number and numbers that are above 68 will get hot,68 will print perfect and below that it will print cold


num=int(input("A number"))
if num % 2 ==0:
    print("It's even")
elif num % 2==1:
    print("It's odd")

bill=float(input("How much was the bill"))
service= input("how was the service")
if service=="ok":
    print(bill*1.15)
elif service=='great':
    print(bill*1.2)
elif service=='amazing':
    print(bill*1.25)
elif service=='horrible':
    print(bill*1)
else:
    print("error")
'''
def factor_num():
    answer=int(input("Insert a factor"))
    for i in range(1,answer+1):
        if answer% i == 0:
            print(f"{i} is a factor of {answer}")
factor_num()
def great_num():
    gcf=1
    answer_num1=int(input("insert a number"))
    answer_num2=int(input("insert another number"))
    limit=min(answer_num1,answer_num2)
    for i in range(1,limit+1):
        if answer_num1%i==0 and answer_num2%i==0:
            print(f'{i}" is a factor of "{answer_num1}+ {answer_num2}')
            gcf=i

great_num()

""" def factor(x,y):
    factor=input("input")
    if factor== x*y:
        for i in range(x,y):
            factor=int(1,factor+1)

def spaces(N,Y,T):

    a=0
    N = int(input("How many spaces? "))
    Y = list(input("Enter day 1 status (C for occupied, . for free): "))
    T = list(input("Enter day 2 status (C for occupied, . for free): "))
    for i in range(N):
        if Y[i]==T[i] and Y[i]=="C":
            a=a+1
print("There are "+ str(a) +" spaces that were free for two days in a row")


def equal_ignore_case(T,S):
    lines=input("Give me a sentence")
    for i in range(len(lines)):
        if lines[i]==T > lines[i]==S:
            print("It's probably French")
        elif lines[i]==T < lines[i]==S:
            print("It's probably English")
        elif lines[i]==T == lines[i]==S:
            print("It's probably French bagetts") """
