a=[1,2,3,4,5,6,7]
n=int(input("enter the number"))
i=0
sum=0
while i<len(a):
    if a[i]>n:
        sum=sum+a[i]
    i=i+1
print(sum)    
