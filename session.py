# t=int(input())
# for i in range(t):
#      c,d,l=map(int,input().split())
#      total=(c+d)*4
#      if(c>(d*2)):
#         min_legs=(c-(d*2)+d)*4
#      else:
#         min_legs=(d*4)
#      if l%4==0 and l>=min_legs and l<=total:
#          print("yes")
#      else:
#           print("no")




# T=int(input())
# for _ in range(T):
#     C,D,L=map(int,input().split())
#     total = (C+D)*4
#     min_no=C-D*2
#     if(total>=L and L%4==0 and (D+min_no)*4<=L):
#         print("yes")
#     else:
#         print("no")



# correct

# t=int(input())
# for i in range(t):
#      c,d,l=map(int,input().split())
#      total=(c+d)*4
#      if(c>(d*2)):
#         min_legs=(c-(d*2)+d)*4
#      else:
#         min_legs=(d*4)
#      if l%4==0 and l>=min_legs and l<=total:
#          print("yes")
#      else:
#           print("no")



# arr=[2,8,3,5,7,4,1,2]
# unit=2
# r=7
# sum=0
# count=0
# for i in range(4):
#     # count=0
#     # if arr[i]<r:
#     rats=r*unit
#     sum+=arr[i]
#     count+=1
# print(count)
# print(rats)
# print(sum)


# arr=[2,8,3,5,7,4,1,2]
# for i in range(5):
#     print(arr[i])



# For input a = 5 & b = 5.
#   function (input a, input b)
#   If (a < b)
#   return function (b, a)
#   elseif (b != 0)
#   return (a * function (a, b - 1))
#   else
#   return 0

# a=5
# b=5
# def sum(a,b):
#     if a<b:
#         return sum(b,a)
#     elif b!=0:
#         return (a*sum(a,b-1))
#     else:
#         return 0


# print(sum(5,5))



# Sum of numbers divisible by 4 are 4 + 8 + 12 + 16 + 20 = 60 Sum of numbers not divisible by
# 4 are 1 +2 + 3 + 5 + 6 + 7 + 9 + 10 + 11 + 13 + 14 + 15 + 17 + 18 + 19 = 150
# Difference 150 – 60 = 90



# n=4
# m=20
# # n=int(input())
# # m=int(input())
# i=1
# sum_4=0
# sum1=0
# for i in range(1,m+1):
#     if i%n==0:
#         sum_4+=i
#     else:
#         sum1+=i
# print(sum1-sum_4)



# def fun(r,unit,arr,n):
#     if n==0:
#         return -1
#     rats=r*unit
#     food=0
#     house=0
#     for i in range(n):
#         food+=arr[i]
#         if food>=rats:
#             break
#     if rats>food:
#         return 0
#     return i+1
# r = int(input())
# unit = int(input())
# n = int(input())
# arr=list(map(int,input().split()))
# print(fun(r,unit,arr,n))


# r="rhutuja"
# h="ajutuhr"
# def anagram():
#     if sorted(r)==sorted(h):
#         return "Yes"
#     else:
#         return "No"
# print(anagram())



