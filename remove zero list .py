a=[403500,5630700,763000,82000]
i=0
b=[]
while i<len(a):
    s=str(a[i])
    sum=""
    j=0
    while j<len(s):
        if s[j]=="0":
            pass
        else:
            sum=sum+s[j]
        j=j+1 
    b.append(int(sum))
    i=i+1
print(b)           

# a=[2,5,2,3,2,7,8,3,9,7,2,0,8]
# i=0
# b=[]
# k=[]
# while i<len(a):
#     s=a[i]!=5,9,0
#     if a[i] not in b:
#      b.append(a[i])
#      k.append[s]
#     i=i+1
# print(b,k)    