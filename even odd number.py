a=[2,4,6,8,3,9,7,5,11,4,17,12]
i=0
b=[]
d=[]
c=0
c1=0
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
        c=c+1
    elif a[i]%2!=0:
        d.append(a[i])
        c1=c1+1
    i=i+1
print(b,c)
print(d,c1)        
          




