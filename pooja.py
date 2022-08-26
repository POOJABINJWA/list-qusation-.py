a=[1111,25,26,31]
i=0
b=[]
while i<len(a):
    d=a[i]%10
    c=a[i]//10
    n=d+c
    b.append(n)
    i=i+1
print(b)    



# [1,2,26,31]

# 4b