even=0
odd=0
a=[]
b=int(input("Enter no of elements="))

for i in range(0,b):
    t=int(input("Enter in list="))
    a.append(t)

for i in a:
    if(i%2==0):
        even+=1
    else:
        odd+=1

print(even)
print(odd)
