# You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12  # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304  # Should return '70000 + 300 + 4'
a="70304"
i=0
while i<len(a):
    j=len(a)-(i+1)
    b=int(a[i])*10**j
    print(b,"+",end="")
    i=i+1