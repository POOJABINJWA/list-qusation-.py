
# a=["m","o","m"]
# a=[1,2,1,1]
# i=0
# rev=1
# while i<len(a):
#     c=a[i]
#     d=a[-rev]
#     i=i+1
#     rev=rev+1
# if d==c:
#     print("polidrom")
# else:
#     print("not")        



# n=["m","o","m"]
n=[1,2,1,1,1,5]
i=0
rev=1
while i<len(n) or rev<len(n):
    d=n[i]
    c=n[-rev]
    i=i+1
    rev=rev+1
if c==d:
    print("polidrom")
else:
    print("not")      