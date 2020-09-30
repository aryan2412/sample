fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)

mydict=dict()
for line in fhandle:
    if not line.startswith('From '):
        continue
    mylist1=line.split()
    print(mylist1)
    mylist2=mylist1[5].split(':')
    mydict[mylist2[0]]=mydict.get(mylist2[0],0)+1

mylist3=sorted((h,c) for h,c in mydict.items())
for h,c in mylist3:
    print(h,c)
