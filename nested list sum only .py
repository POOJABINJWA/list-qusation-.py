a=[2,3,4,5,6,[6,5,4]]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+(a[i][j])
            j=j+1
    i=i+1
print(sum)        