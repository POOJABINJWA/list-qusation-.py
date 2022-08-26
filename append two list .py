a=[10,20,30,40]
b=[100,200,300,400]
i=0
j=1
c=[]
while i<len(a):
    d=a[i],b[-j]
    c.append(d)
    i=i+1
    j=i+1
print(c,end="")    

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


a=[2,2,2,3,1,4,4,5,6,7,5,8,9]
d=[]
i=0
while(i<len(a)):
    j=0
    c=0
    while(j<len(a)):
        if a[i]==a[j]:
          j=j+1
    if c>1:
        d.append(a[i])
        c=c+1
    i=i+1
print(d)
i=0
while i(len(a)):
    j=0
    c=0
    while j<len(a[i]):
        if a[i]==a[j]:
            c=c+1
        j=j+1
    if c>1:
        d.append(a[i])
    i=i+1
print(d,c)
