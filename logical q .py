# a=[8,-2,7,-1,-2,5,6,7]
# i=0
# c=[]
# while i<len(a):
#     if a[i]<0:
#         c.append(0)
#     else:
#         c.append(a[i]) 
#     i=i+1
# print(c)           

a=[1,3,2,4,5,6,7,8,7]
i=0
b=[]
while i<len(a):
    if a[i]%2==0:
        a[i]=1
    else:
        b.append(a[i]) 
    i=i+1
print(b)           