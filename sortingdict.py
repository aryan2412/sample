a={'a':1,'b':20,'c':10}
tmp=list()
for k,v in a.items():
    tmp.append((v,k))

#tmp=sorted(tmp)
tmp=sorted(tmp,reverse=True)
print(tmp)
