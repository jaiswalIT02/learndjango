#from django.test import TestCase

# Create your tests here.
#x=2000

x=2001
if x%4==0:
    print("This is leap year")
else:
    print("This is not leap year")


x=9
if x**0.5==0:
    print("Square")
else:
    print("Not square")


a=4
b=6
c=0

max=a
min=a

if b>max:
    
    max=b
    
if b<min:
    
    min=b
    
if c>max:  
    max=c
if c<min:
    min=c
    
print("Max = ",max)   
print("Min = ",min)
mid=a+b+c-max-min
print("Mid = ",mid)
print(a)



