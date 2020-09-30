b=[]
a=int(input("Enter no of elements in list="))

for i in range(0,a):
    t=input("Enter in list=")
    b.append(t)
temp=b[0]   
for i in range(1,a):
    if(temp>b[i]):
        temp=b[i]

print("smallest number="+temp)        
