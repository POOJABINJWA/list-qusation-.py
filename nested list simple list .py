a=[1,[2],[2,3],[3],4]
i=0
b=[]
while i<len(a):
    if type(a[i])==list :
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)          

# a=[1,2,2,3,3,4]
# i=0
# b=[]
# while i<len(a)-1:
#     h=(a[i],a[i+1])
#     b.append(h)
#     i=i+1
# print(b)