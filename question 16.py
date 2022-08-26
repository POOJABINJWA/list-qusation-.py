# Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
# Original list:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Difference between elements (n+1th - nth) of the said list :
# [1, 1, 1, 1, 1, 1, 1, 1, 1]

a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
j = 1
b=[]
while j < len(a):
    c = a[j]-a[i]
    b.append(c)
    i+=1
    j+=1
print(b)

# qustion16.1=   
# [2, 4, 6, 8]
# Difference between elements (n+1th - nth) of the said list :
# [2, 2, 2]


# d=[2, 4, 6, 8]
# i=0
# j=3
# c=[]
# while j<len(d):
#     b=d[j]-d[i]
#     c.append(b)
#     i=i+1
#     j=j+1
# print(c)    







