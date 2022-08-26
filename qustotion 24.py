# Remove duplicates from a list.
# List = Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# Output: [1,2,3]

a= [1,2,3,1,2,2]
i=0
d=[]
while i<len(a):
    if a[i] not in d:
        d.append (a[i])
    i=i+1
print(d)        


