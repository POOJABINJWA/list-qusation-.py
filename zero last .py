a=[102,106,105,104,108]
i=0
b=[]
while i<len(a):
    k=str(a[i])
    g=""
    h=""
    j=0
    while j<len(k):
        if k[j]!="0":
          g=g+k[j]
        else:
            h=h+k[j]  
        j=j+1
    b.append(int(g+h))
    i=i+1
print(b)            