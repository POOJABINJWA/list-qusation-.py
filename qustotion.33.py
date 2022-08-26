# Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7

# The original list is : [15, 81, 11, 234]
# List Integer Summation : [6,9,2,9]

a=[12,67,98,34]
i=0
e=[]
while i<len(a):
    b=a[i]%10
    d=a[i]//10
    n=b+d
    e.append(n)
    i=i+1
print(e)

# b=[15, 81, 11, 234]
# i=0
# j=[]
# while i<len(b):
#     a=b[i]%10
#     v=b[i]//10
#     w=a+v
#     j.append(w)
#     i=i+1
# print(j)    