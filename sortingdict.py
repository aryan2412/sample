a={'a':1,'b':20,'c':10}
tmp=list()
for k,v in a.items():
    tmp.append((v,k))

asc_tmp=sorted(tmp)
dsc_tmp=sorted(tmp,reverse=True)
print("sorted dictionary in descending order ={}".format(dsc_tmp))
print("sorted dictionary in ascending order ={}".format(asc_tmp))
