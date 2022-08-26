# Given start and end of a range, write a Python program to print all positive numbers in given range.
# Example:
# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5 

# Input: start = -3, end = 4
# Output: 0, 1, 2, 3, 4

# a=[-4,-3,-2,-1,0,1,2,3,4,5]
# i=0
# d=[]
# while i<len(a):
#     if a[i]>0:
#         d.append(a[i])
#     i=i+1
# print(d)   
# 


# qustotion 32.1
#  Input: start = -3, end = 4
# Output: 0, 1, 2, 3, 4

s=[-3,-2,-1,0,1,2,3,4,]
i=0
a=[]
while i<len(s):
    if s[i]>=0:
        a.append(s[i])
    i=i+1
print(a)    
