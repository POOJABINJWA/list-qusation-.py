# Find the First Maximum, Second maximum, Third maximum number from the List.
a=[60 ,40 ,29 , 19 , 20,90]
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
i=0
max1=0
while i<len(a):
    if a[i]>max1  and max!=a[i]:
        max1=a[i]
    i=i+1
i=0
max2=0        
while i<len(a):
    if a[i]>max2  and max1!=a[i] and max!=a[i]:
        max2=a[i]
    i=i+1
print(max)
print(max1)
print(max2)        

                
