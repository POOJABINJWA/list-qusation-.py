# Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]


# a=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#          b.append(a[i])
#     i=i+4
# print(b)       



# QUESTION=25.1
# nput: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
# Output: [4, 3, 6]

d=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
i=0
c=[]
while i<len(d):
    if d[i]not in c:
        c.append (d[i])       
    i=i+1
print(c)        


