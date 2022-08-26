a=[2,2,2,3,1,4,4,5,6,7,5,8,9]
d=[]
i=0
while(i<len(a)):
    j=0
    c=0
    while(j<len(a)):
        if a[i]==a[j]:
            c=c+1
        j=j+1
    if c>1:
        d.append(a[i])
    i=i+1
print(d)