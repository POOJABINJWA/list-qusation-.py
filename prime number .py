a=[2,5,3,7,2,1,6]
i=0
while i<len(a):
    j=1
    c=0
    while j<=a[i]:
        if a[i]%j==0:
            c=c+1
        j=j+1
    if c==2:
        print(a[i],"prime number")
    else:
        print(a[i],"not prime number")                
    i=i+1