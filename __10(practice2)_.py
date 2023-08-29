'''
Q.A company organizes an online poll for its new product by getting the details of the
customer such as name, age and rating of the product. The polled population has to be
organized according to their age (less than or equal to 20 and older than 20).
Implement an algorithm to display the sorted list of customers, according to the
product ratings under both the age categories.
Input 1 : No of customers(N)
Input2 : Name, Age and rating.
Output Format: Two sorted lists
Example Input/Output :
Input: N=5
Customer Details:
Name Age Rating
Cust1 18 8.3
Cust 2 25 9.1
Cust 3 17 8.8
Cust 4 52 7.4
Cust 5 45 8.7
'''
def listt(l):
    l1=[]
    l2=[]
    for i in range(n):
        name,age,rating=l[i][0],l[i][1],l[i][2],
        if age<20:
            l1.append(l[i])
        else:
            l2.append(l[i])
            
    l1.sort(key= lambda x: x[2])
    l2.sort(key= lambda x: x[2])
    return l1,l2
    
n=5
l=[[input(i),int(input(i)),float(input(i))] for i in range(n)]

l1,l2=listt(l)

print("List 1 (Under the age 20)")
for customer in l1:
    print(str(customer).replace("[","").replace("]",""))

print("List 2 (Above the age 20)")
for customer in l2:
    print(str(customer).replace("[","").replace("]",""))

'''
Q.Abe is going to plant „m‟ oak trees and „n‟ pine trees. Abe would like to plant the trees
in rows that all have the same number of trees and are made up of only one type of
tree. What is the greatest number of trees Abe can have in each row? Write a recursive
function to find the solution.
'''
def how(m,n):
    if m==0 or n==0:
        return 0
    else:
        return max(m, n) % min(m, n) 
        
m=int(input("m: "))
n=int(input("n: "))

print(how(m,n))

'''
Q.Given three points, write a program to check if they can form a triangle using the
condition given below:
- Three points can form a triangle, if they do not fall in a straight line and length
of a side of triangle is less than the sum of length of other two sides of the
triangle.
For example, the points (5,10), (20,10) and (15,15) can form a triangle as they do not
fall in a straight line and length of any side is less than sum of the length of the other
two sides
'''
def tri(x1,x2,y1,y2,x3,y3):
    l1=((x2-x1) ** 2+ (y2- y1)** 2 ) ** 0.5
    l2=((x3-x2)** 2 + (y3 - y2) ** 2) ** 0.5
    l3 =((x1-x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    if (x1 * (y2 -y3) + x2 *(y3 -y1) + x3 *(y1 -y2)) ==0:
        return False
    if l1 + l2 >l3 and l2 +l3 >l1 and l1 + l3 >l2:
        return True
    else:
        return False
        

print(tri(5,10,20,10,15,15))

'''
Q.Marks.csv file has the following data: RegNo, Name, Mark1, Mark2 and MArk3 of „n‟
no of students. Write a program to read the data from the file and calculate the total
marks scored by each student. Then copy the content in another file called result.csv
along with the total marks scored by each student.
[Note: use readlines()]
'''
import csv

with open('Marks.csv', 'r') as file:
    lines = file.readlines()

updated_data = []

for line in lines:
    values = line.strip().split(',')

    reg_no = values[0]
    name = values[1]
    marks = list(map(int, values[2:]))

    total_marks = sum(marks)

    updated_data.append([reg_no, name, *marks, total_marks])

with open('result.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerows(updated_data)

'''
Q.Write a function to remove all punctuations in a passage.
'''
import string
p="Hello, world! How are you today?"
print(p.translate(str.maketrans("","",string.punctuation)))

or

n=inputO
n-n. replace(" ,",""). replace("&","") .replace(".",""). replace("?"
,""). replace("!","")
print(n)

'''
Q.
Input:
AAGGTAAGTTGA
Output:
'G': 4, 'A': 5, 'C': 0, 'T': 3
'''
1=input ("inp: ")
d2-{'G': 0, 'A': 0, 'C': 0, 'T': 0} for i in 1:
if i in d2:
d2[i]=1.count(i)
print(d2)

'''
Q.
Input:
Have a great day.
Output:
Have A Great Day
'''
s-input("inp: ")
print(s.title())
#or
s1-s.split(" ") for i in s1:
print(i.capitalize(), end-" ")
















