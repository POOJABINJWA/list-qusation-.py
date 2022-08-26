# Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

# Iist2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1

# b=[2, -7, 5, -64, -14]
# i=0
# c=0
# c1=0
# while i<len(b):
#     if b[i]>0:
#         c=c+1
#     else: 
#         c1=c1+1
#     i=i+1
# print("positive no",c)
# print("negative no",c1)




# QUESTION 30.1
# Iist2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1

d=[-12, 14, 95, 3]
i=0
c=0
c1=0
while i<len(d):
    if d[i]>0:
        c=c+1
    else:
        c1=c1+1
    i=i+1
print("postivie no",c)   
print("negitive no",c1)         
