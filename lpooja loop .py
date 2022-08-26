# i=1
# while i<=100:
#     print(i)
#     i=i+1

# i=1
# while i<=100:
#     if i%7==0:
#         print(i)
#     i=i+1    

# i=1
# sum=0
# while i<=100:
#     sum=sum+i
#     i=i+1    
# print(sum)
     
# i=1
# sum=0
# while i<=10:
#     num=int(input("enter the number"))
#     if i<=num: 
#      sum=sum+num
#     i=i+1
# print(sum)

# i=1
# while i<=100:
#     if i%2==0:
#         print(-i)
#     else:
#         print(i)    
#     i=i+1

# i=1
# while i<=100:
#     if i%3==0 and i%7==0:
#         print(i,"navgurukul")
#     elif i%3==0:
#         print(i,"nav")
#     elif i%7==0:
#         print(i,"gurukul")
#     else:
#         print(i)
    #   i=i+1

# i=61
# while i<=71:
#     print(i-61)
#     i=i+1

# n=int(input("enter the number "))
# i=1
# while i<=n:
#     j=1
#     while j<=10:
#         print(j*i,end="   ")
#         j=j+1
#     print()
#     i=i+1    

# # a=65
# i=1
# while i<5:
#     j=1
#     while j<=i:
#         print(chr(a),end="")
#         j=j+1
#         a=a+1
#     print()
#     i=i+1        


# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end=" ")
#         b=b+1
#     j=i
#     k=2
#     while j>=1:
#         print(j,end=" ") 
#         j=j-1
#     while k<=i:
#         print(k,end=" ")
#         k=k+1
#     print()
#     i=i+1    


# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print("",end="" )
#         b=b+1
#     j=1
#     while j<=i:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1        

# # i=5 
# while i>=1:
#     b=1
#     while b<=i-1:
#         print(" ",end="")
#         b=b+1
#     j=6
#     while j>i:
#         print("*",end="")
#         j=j-1
#     print()
#     i=i-1    

# a=65
# i=1
# while i<5:
#     j=1
#     while j<=i:
#         print(chr(a),end="")
#         j=j+1
#         a=a+1
#     print()
#     i=i+1    

# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end=" ")
#         b=b+1
#     j=i
#     k=2
#     while j>=1:
#         print(j,end=" ")
#         j=j-1
#     while k<=i:
#         print(k,end=" ")
#         k=k+1
#     print()
#     i=i+1    

# a="python"
# i=0
# while i<=5:
#     j=0
#     while j<=i:
#         print(a[j],end="")
#         j=j+1
#     print()
#     i=i+1    

# i=5
# while i>=1:
#     b=1
#     while b<=5-i:
#         print(" ",end="")
#         b=b+1
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i-1    

# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print("",end=" ")
#         b=b+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1
# i=4
# while i>=1:
#     b=1
#     while b<=5-i:
#         print("",end=" ")
#         b=b+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i-1         
# # 
# # 

# # i=0
# # while i<=6:
# #     b=1
# #     while b<=3-i:
# #         print("",end="")
# #         b=b+1
# #     j=0
# #     while j<=6:
# #         if (i+j==3) or (j-i==3) or (i-j==3) or (i+j==9):
# #             print("*",end=" ")
# #         else:
# #             print(" ",end=" ")
# #         j=j+1
# #     print()
# #     i=i+1

# # n=int(input("enter the number :"))
# # c=n
# # sum=0
# # while n>0:
# #     sum=sum+(n%10)*(n%10)*(n%10)
# #     n=n//10
# # if c==sum:
#     print("amstorng")
# else:
#     print("not")        

# n=int(input("enter the number"))
# a=n
# rem=0
# sum=0
# while n>0:
#     rem=n%10
#     sum=sum+rem
#     n=n//10
# if a%sum==0:
#     print("harshad")
# else:
#     print("not")    


# n=int(input("enter the number"))
# c=n
# rev=0
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# if c%rev==0:
#     print("polidrom")
# else:
#     print("not")        

n=int(input("enter the number "))
cunat=0
i=1
while i<=n:
    if n%i==0:
        cunat=cunat+1
    i=i+1
if cunat==2: 
    print("prime")
else:
    print("not")       


# n=int(input("enter the number "))
# c=n
# i=1
# sum=0
# while i<n:
#     if n%i==0:
#         sum=sum+i
#     i=i+1
# if c==sum:
#     print("perfect") 
# else:
#     print("not") 





# i=1
# s=0
# while i<=10:
#     if i<=5:
#         s=s+i
#         print(s)
#     elif i>=5:
#         print(i*i) 
#     i=i+1       

# n=int(input("enter the number"))
# i=0
# sum=0
# while n>0:
#     b= n%10
#     sum=sum+b*2**i
#     n=n//10
#     i=i+1
# print(sum)    


# i=0
# while i<=10:
#     i=i+1
#     if i==3:
#         print(i,"continue")
#         continue
#     elif i==6:
#          print(i,"pass")
#         pass
#     elif i==8:
#         print(i,"break")
#         break
#     else:
#         print(i)
#     i=i+1
    

# day=int(input("enter the day :"))
# month=int(input("enter the month :"))
# year=int(input("enter the year :"))
# if day>=1 and day<=30:
#     print("day",day+1)
#     if day>=1 and day<=32:
#       print("day",day-1)
#     if month>=1 or month<=12:
#         print("month", month)
#         if year>=2000 or year<=2022:
#             print("year", year)
# else:
#     print("no")        

# a[i]
#     i=i+1
# print(b)    




