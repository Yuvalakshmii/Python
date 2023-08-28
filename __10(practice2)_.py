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


Q.
