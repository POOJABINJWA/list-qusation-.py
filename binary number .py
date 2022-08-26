a=[1,0,1,0,0,1]
i=1
c=0
sum=0
while i<len(a):
    sum=a[-i]*2**c+sum
    c=c+1
    i=i+1
print(sum)


a=[1,3,4,6,7,8,9]
i=0
b=[]
while i<len(a):
    d=a[i]*2
    b.append(d)
    i=i+1
print(b)    
