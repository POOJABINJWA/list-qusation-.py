# a=[0,0,2,0,2,3,5]
# i=0
# c=[]
# while i<len(a):
#     if a[i]!=0:
#         c.append(a[i])
#     i=i+1
# print(c)        

a=[0,0,2,0,2,3,5]
i=0
c=[]
b=[]
while i<len(a):
    if a[i]==0:
        c.append(a[i])
    else:
        b.append(a[i])
    i=i+1
print(b+c)


