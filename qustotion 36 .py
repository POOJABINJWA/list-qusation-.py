# Write a Python program to join adjacent members of a given list.
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
# Original list:
# ['1', '2', '3']
# Join adjacent members of a given list:
# ['12']

a= ['1', '2', '3', '4', '5', '6', '7', '8']
i=0
d=[]
while i<len(a):
    b=a[i]+a[i+1]
    d.append(b)
    i=i+2
print(d)    

