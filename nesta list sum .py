a=[2,3,4,5,6,[6,5,4,3],5]
i=0
sum=0
while i<len(a):
    if type(a[i])== list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        sum=sum+a[i]        
    i=i+1
print(sum)            
