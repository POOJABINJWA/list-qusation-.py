a=[2,4,6,8,3,9,7,5,11,4,17,12]
i=0
b=[]
d=[]
c=0
c1=0
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
        c=c+1
    elif a[i]%2!=0:
        d.append(a[i])
        c1=c1+1
    i=i+1
print(b,c)
print(d,c1)        
            


# i=1
# while i<=50:
#     if i%3==0 and i%5==0:
#         print(i,"pooja binjwa")
#     elif i%3==0:
#         print(i,"pooja")
#     elif i%5==0:
#         print(i,"binjwa")
#     else:
#         print(i,"not")
#     i=i+1




