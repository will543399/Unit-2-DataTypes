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
'''

num=int(input("A number"))
if num % 2 ==0:
    print("It's even")
elif num % 2==1:
    print("It's odd")

bill=input("How much was the bill")




