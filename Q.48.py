
# Write a Python program to split a given list into specified sized chunks. 
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the said list into equal size 3
# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 4
# [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 5
# [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]


a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
n=0
b=[]
while i<len(a):
    j=0
    c=[]
    while j<5 and n!=len(a):
        c.append(a[n])
        j=j+1
        n=n+1
    b.append(c)
    if n==len(a):
        break 
    i=i+1
print(b)       

   


