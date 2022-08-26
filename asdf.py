a=[1,2,3,4,4]
b=[2,4,3,2,4]
i=0
c=[]
while i<len(a):
    if a[i] not in b:
        j=0
        while j<len(b):
            if a[j] not in c:
                c.append(a[j][i])
                j=j+1
    else:
        c.append(a[i])
    i=i+1
print(c)  


a=[1,2,3,4]
b=a
a.append(4)
print(b)
