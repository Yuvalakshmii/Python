#if statement marks calc

mark=int(input())
if mark>=50:
    print("pass")
else:
    print("fail")

#grade calc
if mark>=90:
    print("S grade")
elif mark>= 80:
    print("A grade")
elif mark>=70:
    print("B grade")
elif mark>=60:
    print("C grade")
elif mark>=55:
    print("D grade")
elif mark>=50:
    print("E grade")
else:
    print("F grade")

#remark for marks
    
mark2=int(input())
print("remarks")
if mark >=90 and mark2 >=90:
    print("excellent")
elif mark >=90 or mark2 >=90:
    print("good")
else :
    print("need to improve")
    
#finding max num
    
a=int(input())
b=int(input())
c=int(input())
maxnum=(a if(a>c) else c)if(a>b) else (b if(b>c) else c)

#calculate charge for internet consumption

hour=int(input())
minn=int(input())
if(hour>7):
    print("invalid input")
    charge=0
else:
    if(hour==5):
        charge=200+minn
    elif(hour<5):
        charge=hour*50+minn
    elif(hour>5):
        charge=200+(hour-5)*50+minn
print("charge",charge)

#while loop eg
a=21
while a<31:
    print(a)
    a+=1

#reversing a number

n=int(input())
a=n
rev=0
while n!=0:
    m=n%10
    rev=rev*10+m
    n=n//10
print("reversed number is",rev,"\n")

#palindrome
print("given number",a)
if a==rev:
    print("palindrome number")
else:
    print("not a palindrome")
    
