# For example, if we give 9119  the function should return  811181, as the  square of 9 is 81 and square of 1  is 1.
# a="9119"
a=int(input("enter the number"))
i=0
while i<len(a):
    b=int(a[i])**2
    print(b,end="")
    i=i+1
