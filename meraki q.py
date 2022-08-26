# s=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# while i<len(s):
#     i=i+1
# print(i)    





# a=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# while i<len(a):
#     if a[i]>=20 and a[i]<40:
#         print(a[i])
    # i=i+1

# a = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# max=0
# i=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# print(max)
# 
# a = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# max1=0
# max2=0
# while i<len(a):
#     if a[i]>max1:
#         max1=a[i]
#     elif a[i]>max2:
#         max2=a[i]    
#     i=i+1    
# print(max1,max2)      

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=0
# while i<len(places):
#     i=i+1
#     print(places[-i])


# a=[1,2,3,4,5,6,7,8,8]
# i=0
# while i<len(a):
#     i=i+1
#     print(a[-i],end=" ")




    

# n=["m","o","m"]
# i=len(n)
# r=[]
# while i>0:
#     r.append(n[i-1])
#     i=i-1
# if r==n:
#     print("yes")
# else:
#     print("no")
         
# # n=["m","o","m"]
# # n=[1,2,1]
# # i=0
# # rev=1
# # while i<len(n) or rev<len(n):
# #     d=n[i]
# #     c=n[-rev]
# #     i=i+1
# #     rev=rev+1
# # if c==d:
# #     print("polidrom")
# # else:
# #     print("not")        

# # a= [1, 0, 1,0]
# # i=-1
# # c=0
# # sum=0
# # while i>=-len(a):
# #     sum=sum+a[i]*2**c
# #     c=c+1
# #     i=i-1
# # print(sum)      



# # b = [1, 0, 0, 1]
# # i=-1
# # c=0
# # sum=0
# # while i>=-len(b):
# #     sum=sum+b[i]*2**c
# #     c=c+1
# #     i=i-1
# # print(sum)    

# # r = [1, 0, 0, 0, 1]
# # i=-1
# # c=0
# # sum=0
# # while i>=-len(r):
# #     sum=sum+r[i]*2**c
# #     c=c+1
# #     i=i-1
# # print(sum)    



# # a = [1,2,3,4,5,6] 
# # b= [2,3,1,0,6,7]
# # i=0
# # c=[]
# # while i<len(a):
# #     if a[i] not in (b):
#         c.append(a[i])
#     i=i+1
# print(c)


# m = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# i=0
# sum=0
# while i<len(m):
#     j=0
#     while j<len(m[i]):
#         sum=sum+m[i][j]
#         j=j+1
#         print(sum)
#         i=i+1




# s = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# c=[]
# v=[]
# while i<len(s):
#     if s[i]%2==0:
#         c.append(s[i])
#     else:
#          v.append(s[i])
#     i=i+1
# print(c)
# print(v)

m = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
c=[]
v=[]
while i<len(m):
    if m[i]%2==0:
        sum=sum+m[i]
        c.append(m[i]) 
    else:
        sum1=sum1+m[i]
        v.append(m[i]) 
    i=i+1
print(c,sum)
print(v,sum1)           


# s = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# sum1=0
# c=0
# c2=0
# while i<len(s):
#     if s[i]%2==0:
#         sum=sum+(s[i])
#         c=c+1
#     else:
#         sum1=sum1+s[i]
#         c2=c2+1
#     i=i+1
# print(sum,c,sum/c)    
# print(sum1,c2,sum1/c2)


# a=[23, 14 ,56,12,19,9,15,25,31,42,43]
# i=0
# c=0
# c1=0
# c2=0
# sum=0
# sum1=0
# sum2=0
# avg=0 
# avg1=0
# avg2=0
# while i<len(a):
#     if a[i]%2==0:
#         print("even number")
#         sum=sum+a[i]
#         c=c+1
#         avg=sum/4
#     if a[i]%2!=0:
#         print("odd number")
#         sum1=sum1+a[i]
#         c1=c1+1
#         avg1=sum1/7 
#     if a[i]%1==0:
#         sum2=sum2+a[i]
#         c2=c2+1
#         avg2=sum2/11       
#     i=i+1
# # # print(c)  
# # # print(c1)
# # # print(c2)
# # # print(sum)
# # # print(sum1)
# # # print(sum2)
# # # print(avg)
# # # print(avg1)
# # # print(avg2)
# print(c,sum,avg)
# print(c1,sum1,avg1)
# print(c2,sum2,avg2)


# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# a=[]
# while i<len(n):
#     if n[i] not in a:
#         a.append(n[i])
#     i=i+1
# print(a)        

# a=[15,16,17,18,19]
# i=-1
# while i>=-len(a):
#     print(a[i],end=" ")
#     i=i-1