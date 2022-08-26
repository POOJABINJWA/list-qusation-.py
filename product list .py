# Qustoin=1
# Iterate over both the values in a list and their indicesgrocery_list = ['flour','cheese','carrots']
# g = ['flour','cheese','carrots']
# i=0
# while i<len(g):
#     print(i,g[i])
#     i=i+1

# QUESTION=4List product excluding duplicates.
    # List = [6,1,3,5,6,3,1]
    # Output: 60

a = [6,1,3,5,6,3,1]
i=0
pro=1
b=[]
while i<len(a):
    if a[i] not in b:
        pro=pro*a[i]
        b.append(a[i])

    i=i+1
print(pro)    





