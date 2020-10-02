even=0
odd=0
a=[]
b=int(input("Enter no. of elements="))   #User Input for list size


for i in range(0,b):
    t=int(input("Enter in list="))       #User Input for elements of List
    a.append(t)

    
for i in a:
    if(i%2==0):
        even+=1
    else:
        odd+=1