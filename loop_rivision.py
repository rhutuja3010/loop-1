# user=int(input("enter the number :"))
# rev=0
# while user>0:
#     rem=user%10
#     rev=rev*10+rem
#     user=user//10
# print(rev)


# a=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
# n=int(input("enter the number :"))
# i=0
# while i<len(a):
#     if i==n:
#         print(a[i])
#     i+=1




# i=10
# while i>0:
#     print(i)
#     i-=1
    

# i=100
# sum=0
# while i>=1:
#     sum+=i
#     i-=1
#     print(sum)


# n=int(input("enter the number :"))
# i=0
# while i<1:
#     b=n-10
#     print(10,"+",b)
#     i+=1

# fabonacciseries
# f=int(input("enter the number :"))
# x=0
# y=1
# z=0
# while z<=f:
#     print(z)
#     x=y
#     y=z
#     z=x+y

# i=0
# sum=0
# while i<4:
#     l=int(input("enter the number :"))
#     sum+=l
#     i+=1
# print(sum)

# i=1
# while i<=100:
#     if i%2==0:
#         print(-i)
#     else:
#         print(i)
#     i+=1

# i = 891
# while i < 931:
#     z = i - 890
#     if z % 3 == 0:
#         print(z)
#     i = i + 1   


# i=31
# while i<=41:
#     a=i-30
#     print(a)
#     i+=1

# s="my name is"
# i=0
# l=[]
# while i<len(s):
#     if s[i]!=" ":
#         l.append(s[i])
#         # a="".join(l)
#     i+=1
# print(l)


# a = -1
# while a >= (-10):
#     print (-a)
#     a = a -1


# i=-1
# while i>=-10:
#     print(-i)
#     i-=1


# i=1
# while i<=100:
#     if i%3==0 and i%7==0:
#         print("navgurukul")
#     elif i%3==0:
#         print("nav")
#     elif i%7==0:
#         print("gurukul")
#     else:
#         print(i)
#     i+=1

# Make a program to print the numbers from 11 to 101. The loop counter should start from 156.
# i=156
# while i<166:
#     a=i-155
#     print(a)
#     i+=1

# n=int(input("enter no :"))
# i=1
# sum=0
# while i<=n:
#     a=int(input("enter : "))
#     sum+=i
#     i+=1
# print(sum)


# i=1
# count=0
# number=int(input("enter no :"))
# while i<=number:
#     if number%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("it is prime no")
# else:
#     print("not prime")

# n=(input("enter the number :"))
# b=""
# i=0
# while i<len(n):
#     b+=n[i]
#     j=1
#     while j<=(len(n)-(i+1)):
#         b+="0"
#         j+=1
#     if i==(len(n)-1):
#         break
#     else:
#         b+="+"
#     i+=1
# print(b)

# n=input("enetr no :")
# i=0
# b=""
# while i<len(n):
#     j=0
#     b+=n[i]
#     while j<=len(n)-(i+1):
#         b+="0"
#         j+=1
#     if i==len(n)-1:
#         break
#     else:
#         b+="+"
#     i+=1
# print(b)

# a="i im Rhutuja"
# i=0
# l=[]
# while i<len (a):
#     if a[i]!=" ":
#         l.append(a[i])
#     i+=1
# print(l)

# def n(num):
#     if num%10!=0:
#         print(num)
#     else:
#         n(num=num//10)
# n(int(input("enter the no :")))
# n(1200)

# n=int(input("enter "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j+=1
#     i+=1
#     print()
# a=5                                               # *
# i=0                                            #* *
# while i<=a:                                  # * * *
#     j=1                                     # * * * * 
#     while j<=a-i:                           #* * * * *
#         print(" ",end="")
#         j+=1
#     k=0
#     while k<=i:
#         print("*",end=" ")
#         k+=1
#     i+=1
#     print()

# i=0                                            #* *
# while i<=5:                                  # * * *
#     j=1                                     # * * * * 
#     while j<=5-i:                           #* * * * *
#         print(" ",end="")
#         j+=1
#     k=0
#     while k<=i:
#         print("*",end="")
#         k+=1
#     i+=1
#     print()

# i=0                                            #* *
# while i<=5:                                  # * * *
#     j=1                                     # * * * * 
#     while j<=5-i:                           #* * * * *
#         print("*",end=" ")
#         j+=1
#     k=0
#     while k<=i:
#         print("*",end=" ")
#         k+=1
#     i+=1
#     print()

# n=int(input("enetr "))
# for i in range(n):
#     print(i*"*")
    # print()


# Q6.
# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# a={"0":10,"1":20}
# for i in a:
#     # print(a[i])
#     # e=i+i
#     f=a[i]+10
#     a.update({i:f})
# print(a)

# a=[5,10,15,25]
# print(a[::-2])
# m=5
# l=1
# while l<=5:
#     n=1
#     while n<=m-l:
#         print(" ",end="")
#         n+=1
#     g=1
#     while g<=l:
#         print('*',end=" ")
#         g+=1
#     l+=1
#     print()

# a=5
# i=1
# while a>0:
#     j=1
#     while j<i:
#         print(" ",end="")
#         j+=1
#     k=1
#     while k<=a:
#         print("*",end=" ")
#         k+=1
#     print()
#     a-=1
#     i+=1


# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     i+=1
#     print()


# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print("",end="")
#         print(j,end=" ")
#         j+=1
#     i-=1
#     print()



# for i in range(5):
#     for j in range(5):
#         if i-j==2 or j-i==2 or i==1 and j==1 or i==3 and j==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# row= int(input("enter the number of row :"))
# for i in range(row):
#     print(" "*(row-i)+" *"*(i+1))
# for j in range(row-1):
#     print(" "*(j+2)+" *"*(row-1-j))

# row= int(input("enter the number of row :"))
# for i in range(row):
#     print(" "*(row-i)+" *"*(i+1))
# for j in range(row-1):
#     print(" "*(j+2)+" *"*(row-1-j))

# a=5
# i=0
# while i<=a:
#     j=1
#     while j<=a-i:
#         print(" ",end="")
#         j+=1
#     k=0
#     while k<=i:
#         print("*",end=" ")
#         k+=1
#     i+1
#     print()

# a=5                                               # *
# i=0                                            #* *
# while i<=a:                                  # * * *
#     j=1                                     # * * * * 
#     while j<=a-i:                           #* * * * *
#         print(" ",end="")
#         j+=1
#     k=0
#     while k<=i:
#         print("*",end=" ")
#         k+=1
#     i+=1
#     print()



# a=5

# i=1
# while i<=a:
#     j=0
#     while j<a-i:
#         print("",end=" ")
#         j+=1
#     k=0
#     while k<=i:
#         print("*",end=" ")
#         k+=1
#     i+=1
#     print()
# i=1
# while a>0:
#     j=1
#     while j<i:
#         print(" ",end="")
#         j+=1
#     k=1
#     while k<=a:
#         print("*",end=" ")
#         k+=1
#     print()
#     a-=1
#     i+=1

# i=1
# while a>0:
#     j=1
#     while j<i:
#         print(" ",end="")
#         j+=1
#     k=1
#     while k<=a:
#         print("*",end=" ")
#         k+=1
#     print()
#     a-=1
#     i+=1


# a=5
# i=1
# while a>0:
#     j=1
#     while j<i:
#         print(" ",end="")
#         j+=1
#     k=1
#     while k<=a:
#         print("*",end=" ")
#         k+=1
#     print()
#     # i+=1
#     a-=1
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=6-i:
#         print(i,end=" ")
#         j+=1
#     i+=1
#     print()


# i=5
# while i>=1:
#     j=5
#     while j>=i:
#         print(j,end=" ")
#         j-=1
#     print()
#     i-=1

# i=65
# while i<=69:
#     j=65
#     while j<=i:
#         print(chr(j),end="")
#         j+=1
#     print()
#     i+=1

# i=65
# while i<=69:
#     j=65
#     while j<=69:
#         print(chr(i),end=" ")
#         j+=1
#     print()
#     i+=1


# i=65
# while i<=69:
#     j=i
#     while j<=69:
#         print(chr(j),end=" ")
#         j+=1
#     print()
#     i+=1

# a=65
# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(chr(a),end=" ")
#         j+=1
#         a+=1
#     print()
#     i+=1


# string=input("enter the string :")
# i=0
# while i<len(string):
#     j=0
#     while j<=i:
#         print(string[j],end=" ")
#         j+=1
#     print()
#     i+=1

# i=1
# k=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end="")
#         b+=1
#     j=1
#     while j<=k:
#         print(i,end="")
#         j+=1
#     k+=2
#     print()
#     i+=1

# n=input("enter the string :")
# i=0
# while i<len(n):
    # a=n.upper()
    # b=n.lower()
    # j=0
    # while j<=i:
    #     print(a[i],end="")
    #     break
    # k=0
    # while k<=i:
    #     print(b[i],end="")
    #     k+=1
    # l=0
    # while l<=i:
    #     print("_",end="")
    #     l+=1
    # print()
    # i+=1

# s="rhutuja"
# i=0
# while i<len(s):
#     a=s.upper()
#     b=s.lower()
#     j=0
#     while j<1:
#         print(a[i],end="")
#         j+=1
#     k=0
#     while k<=i:
#         print(b[i],end="")
#         k+=1
#     l=0
#     while l<=i:
#         print("_",end=" ")
#         l+=1
#     print()
#     i+=1

# s="sakshi"
# i=0
# while i<len(s):
#     print(s[i].upper()+s[i].lower()*i+"_",end="")
#     i+=1


# i=5
# while i>=1:
#     j=1
#     while j<=5:
#         print(i,end=" ")
#         j+=1
#     i-=1
#     print()

# i=5
# while i>=1:
#     j=1
#     while j<=5:
#         print(i,end=" ")
#         j+=1
#     i-=1
#     print()

# index = 0
# while 1:
#     print(index," ",end = ""),
#     index=index+1
#     if index == 10:
#         break
# print("Found at",index,"location")


# i=0
# while i<=10:
#     i+=1
#     if i==8:
#         continue
#     print(i)


# Write a code that calculates the sum of those numbers from 30 to 420 which are multiples of 
# 8 that means those numbers come in the table of 8.
# Edit on Github

# i=30
# sum=0
# while i<=420:
#     if i%8==0:
#         sum+=i
#         # print(sum)
#     i+=1
# print(sum)
        

# n=5
# i=0
# sum=0
# while i<=n:
#     r=int(input("enter :"))
#     sum+=r
#     i+=1
# print(sum)
# avg=sum/5
# print(avg)

# i=1
# while i<=100:
#     if i%2==0:
#         print(-i)
#     else:
#         print(i)
#     i+=1

# i = 1
# sum=0
# while i <= 140:
#     if i % 3 == 0:
#         sum = sum + i
#     i = i + 1
# print(sum) 


# # i = 0
# num = int(input("Enter your number:- "))
# # while(i <= num):
# if(num > 0):
#     print("it is positive")
# elif(num < 0):
#     print("it is negetive")
# else :
#     print("zero")
#     # i = i + 1
    # break

# n=5
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y

# p=int(input("enter :"))
# i=1
# count=0
# while i<=p:
#     if p%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("prime")
# else:
#     print("not")


# i=1
# while i<=10:
#     j=1
#     while j<=10:
#         print(i*j,"  ",end=" ")
#         j+=1
#     i+=1
#     print()

# n=2
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

# num=int(input("enter the no :"))
# sum=0
# while num>0:
#     sum=sum+num%10
#     num=num//10
# print(sum)


# num=int(input("enter t :"))
# rev=0
# while num>0:
#     rev=rev*10+num%10
#     num=num//10
# print(rev)


# n=int(input("enter" ))
# fac=1
# while n>0:
#     fac=fac*n
#     n=n-1
#     print(fac)



# n=int(input("enter "))
# fac=1
# while n>0:
#     fac=fac*n
#     n-=1
# print(fac)


# def calculator(number_x,number_y,operation):
#     if operation == "multiply":
#         return (number_x * number_y)
#     elif operation ==  "add":
#         return (number_x + number_y)
#     elif operation== "divide":
#         return(number_x / number_y)
#     elif operation== "substract":
#         return (number_x - number_y)
# a=int(input("Enter a number :"))
# b=int(input("Enter a number :"))
# c=input("enter a operation :")
# d=calculator(a,b,c)
# print(d)


# a=int(input("enter "))
# i=1
# sum=0
# while i<a:
#     if a%i==0:
#         sum+=i
#     i+=1
# if sum==a:
#     print("perfect")
# else:
#     print("not")


# g=int(input("enter the guss :"))
# i=1
# while i<3:
#     if g==3:
#         print("congratulation")
#         break
#     else:
#         print("sorry")
#     a=int(input("enter "))
#     if a==3:
#         print("con")
#         break
#     i+=1


# n=int(input("enter the number :"))
# tem=n
# sum=0
# while tem!=0:
#     rem=tem%10
#     sum+=rem
#     tem=sum//10
# if n%sum==0:
#     print("harshad")
# else:
#     print("not")

# s1="csworld.com"
# s2=""
# s3=""
# for x in s1:
#     if(x=="s" or x=="n" or x=="p"):
#         s2+=x
#     print(s2,end=" ")
#     print(s3)

# a=[1,2,3,4,5,6]
# i=0
# l=[]
# while i<len(a)-1:
#     b=[a[i],a[i+1]]
#     l.append(b)
#     i+=1
# print(l)

# string=input("enter the string :" )
# l1=[]
# l2=[]
# letter="abcdefghijklmnopqrstuvwxyz"
# letter2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# count=0
# count2=0
# i=0
# while i<len(string):
#     if string[i] in letter or string[i] in letter2:
#         l1.append(string[i])
#         count+=1
#     else:
#         l2.append(string[i])
#         count2+=1
#     i+=1
# print( "string :",string)
# print(l1)
# print(l2)
# print("no of letters :",count)
# print("no of digit :",count2)


# Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.

# a= [1, 2, 2, 5, 8, 4, 4, 8]
# l=[]
# i=0
# while i<len(a):
#     if i not in l:
#         l.append(a[i])
#     i+=1
# print(l)


# Write a Python program to create a list reflecting the modified run-length encoding from
# a given list of integers or a given list of characters.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# a= [1,5, 1, 2, 3, 4, 4, 5]
# s=[]
# for i in a:
#     count=0
#     l=[]
#     for j in a:
#         if a[i]==a[j]:
#             count+=1
#     l.append(count)
#     if i not in l:
#       l.append(i)
#     if l not in s:
#         s.append(l)
# print(s)


# a= [1, 5, 1, 2, 3, 4, 4, 5]
# s=[]
# for i in a:
#     count=0
#     l=[]
#     for j in a:
#         if a[i]==a[j]:
#             count+=1
#     l.append(count)
#     if i not in l:
#       l.append(i)
#     if l not in s:
#         s.append(l)
# print(s)

# Convert Character Matrix to single String;
# The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest

# a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# for i in a:
#     for j in a:
# a=["q","e","y"]
# print("".join(a))

# txt = "welcome to the jungle"
# x = txt.split()
# print(x) 



# i=1
# count=0
# num=int(input("enetr the the number :"))
# while i<=num:
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("prime")
# else:
#     print("not")


# i=int(input("enter no :"))
# sum=0
# ori=i
# while i>0:
#     sum=sum+(i%10)*(i%10)*(i%10)
#     i=i//10
# if ori==sum:
#     print("armstrong")
# else:
#     print("not")


# a=[[3,5,6],[2,3],[1],[8,9,0,4]]
# l=[]
# i=0
# while i<len(a):
#     b=len(a[i])
#     l.append(b)
#     i+=1
# print(l)

# a=[[3,5,6], [2,3],[1],[8,9,0,4]]
# # l=[]
# for i in range(len(a)):
#     b=len(a[i]) 
#     # l.append(b)
#     print(b)


## Armstrong number##
# j=153
# l=[]
# while j<=1000:
#     i=j
#     a=i
#     sum=0
#     while i>0:
#         sum=sum+(i%10)*(i%10)*(i%10)
#         i=i//10
#     if a==sum:
#         l.append(a)
#     j+=1
# print(l)


##prime number##
# num=1
# l=[]
# while num<=1000:
#     i=1
#     count=0
#     while i<=num:
#         if num%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         l.append(num)
#     num+=1
# print(l)

# string=input("enter string :")
# i=0
# while i<len(string):
#     a=string.upper()
#     print(a[i]+string[i],end="_")
#     i+=1


# s="Rhutuja"
# i=0
# while i<len(s):
#     print(s[i].upper()+s[i].lower()*i+"_",end="")
#     i+=1


# r="rhutuja"
# i=0
# while i<len(r):
#     print(r[i].upper()+r[i].lower()*i+('_')*i)
#     i+=1


# a=[1,2,3,1,2,3,4,5,1,2,6]
# a=[1,1,1,1,2,2,2,2,3,3,3,3]
# l=[]
# for i in a:
#     if i not in l:
#         l.append(i)
# print(l)

# r=[1,1,1,1,2,2,2,2,3,3,3,3]
# i=0
# l=[]
# while i<len(r)-3:
#     if r[i]==r[i+1]==r[i+2]==r[i+3]:
#         print(r[i])
#     i+=1
# # print(l)
        

# a=[3,5,7,9,45,2,4]

# i=0
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i+=1
# print(max)

# a=["rhutuja"]
# l=[]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if i==0:
#             l.append(a[i][j])
# print(l)
        

# a=["rhutuja"]
# l=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         l.append(a[i][j])
#         j+=1
#     i+=1
# print(l)

# a="1.2"
# a=float(a)
# a=int(a)
# print(complex(a))

# a=[3,1,5,6,7,2,4,8,0,9]
# for j in range(len(a)):
#     for i in range(len(a)-1):


# amount=int(input("enter the amount :"))
# if amount>=1 or amount<=2:
#     print("note of 1 ruppes :",amount//1)
#     if amount>=2 or amount<=5:
#         print("note of 2 ruppes :",amount//2)
#         if amount>=5 or amount<=10:
#             print("note of 5 ruppes :",amount//5)
#             if amount>=10 or amount<=20:
#                 print("note of 10 ruppes :",amount//10)
#                 if amount>=20 or amount<=50:
#                     print("note of 20 ruppes :",amount//20)
#                     if amount>=50 or amount<=100:
#                         print("note of 50 ruppes :",amount//50)
#                         if amount>=100 or amount<=200:
#                             print("note of 100 ruppes :",amount//100)
#                             if amount>=200 or amount<=500:
#                                 print("note of 200 ruppes :",amount//200)
#                                 if amount>=500 or amount<=1000:
#                                     print("note of 500 ruppes :",amount//500)
#                                     if amount>=1000 or amount<=2000:
#                                         print("note of 1000 ruppes :",amount//1000)
#                                         if amount>=2000:
#                                             print("note of 2000 ruppes :",amount//2000)
#                                         else:
#                                             print("1")
#                                     else:
#                                         print("2")
#                                 else:
#                                     print("3")
#                             else:
#                                 print("4")
#                         else:
#                             print("5") 
#                     else:
#                         print("6")
#                 else:
#                     print("7") 
#             else:
#                 print("8") 
#         else:
#             print("9")
#     else:
#         print("10")     
# else:
#     print("11")
                    
# a=[3,4,5,6,9,1,6,8]
# l=[]
# i=0
# while i<len(a)-1:
#     b=a[i+1]-a[i]
#     l.append(b)
#     i+=1
# print(l)            


# a=[[1,6,9],[4,7,2],[5,2,9]]
# l=[]
# sum1=0
# sum2=0
# sum3=0
# for i in range(len(a)):
#     for j in range(len(a)):
#         if j==0:
#             sum1+=a[i][j]
#         if j==1:
#             sum2+=a[i][j]
#         if j==2:
#             sum3+=a[i][j]
# print(sum1)
# print(sum2)
# print(sum3)

# a=[[1,6,9],[4,7,2],[5,2,9]]
# l=[]
# sum1=0
# sum2=0
# sum3=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if i==0:
#             sum1+=a[i][j]
#         if i==1:
#             sum2+=a[i][j]
#         if i==2:
#             sum3+=a[i][j]
#         j+=1
#     i+=1

# print(sum1)
# print(sum2)
# print(sum3)






# def swap(l,a,b):
#     l[a],l[b]=l[b],l[a]
#     return l
# l=[12,19,5,6,10]
# a,b=1,3
# print(swap(l,a-1,b-1))







# a=[[2,0,4],[5,8],[1,9,3,6],[8,6]]
# i=0
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
    #     sum+=(a[i][j])
    #     j+=1
    # i+=1
    # print(sum)



# a=[[2,0,4],[5,8],[1,9,3,6]]
# for i in range(len(a)):
#     sum=0
#     for j in range(len(a[i])):
#         sum=sum+(a[i][j])
#     print(sum)


# a=[1,0,8,[4,6],2,3]
# i=0
# l=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             l.append(a[i][j])
#             j+=1
#     else:
#         l.append(a[i])
#     i+=1
# print(l)

# a=["a","b","c","d"]
# l=[]
# i=0
# while i<=len(a):
#     l.append(a[-i])
#     i+=1
# print(l)


# i=10
# a=[]
# while i>10:
#     print("enter no :")
#     num=input()
#     a.append(num)
#     i-=1
# b=a
# b.reverse()
# print(b)


# i=10
# l=[]
# while i>0:
#     print("enter :")
#     num=input()
#     l.append(num)
#     i-=1
# b=l
# b.reverse()
# print(b)

# mark=["23","56","78","98","45"]
# i=0
# t=0
# while i<len(mark):
#     t+=int(mark[i])
#     i+=1

# print(t)

# a=["rhutuja","shit"]
# i=0
# while i<len(a):
#     print(a[i],":",len(a[i]))
#     i+=1

# e=[2,3,4,6,77,88,12,34,55]
# i=0
# a=0
# b=0
# while i<len(e):
#     if e[i]%2==0:
#         print(e[i],"even")
#         a+=e[i]
#     else:
#         print(e[i],"odd")
#         b+=e[i]7,88,12,34,55]
# i=0
# a=0
# b=0
# while i<len(e):
#     if e[i]%2==0:
#         print(e[i],"even")
#         a+=e[i]
#     else:
#         print(e[i],"odd")
#         b+=e[i]
#     i+=1

# a=[1,0,0,1,1,0,1,1]
# i=1
# j=0
# sum=0
# while i<=len(a):
#     d=a[-i]
#     sum=sum+(2**j)*d
#     j+=1
#     i+=1
# print(sum)

# s=input("enetr :")
# i=0
# while i<len(s):
#     print(s[0].upper(),s[i].lower(),end="_")
#     i+=1


# s="my name is"
# i=0
# l=[]
# while i<len(s):
#     if s[i]!=" ":
#         l.append(s[i])
#         # a="".join(l)
#     i+=1
# print(l)
# # print(a)


# r="my name is Rhutuja"
# i=0
# l=[]
# while i<len(r):
#     if r[i]!=" ":
#         l.append(r[i])
#         a="".join(l)
#     i+=1
# print(l)
# print(a)



# a=["Rhutuja"]
# l=[]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         l.append(a[i][j])
# print(l)


# def apppend():
#     a=[3,4]
#     print(a+[6])
# apppend()


# a=[2,3,5,1,3,4,6,8,1,2,1]
# i=0
# l=[]
# while i<len(a):
#     if a[i] not in l:
#         l.append(a[i])
#     i+=1
# print(l)



# a=["r","h","u","t","u","j","a"]
# i=0
# list1=[]
# while i<len(a):
#     j=0
#     list2=[]
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count+=1
#         j+=1
#     list2.append(a[i])
#     list2.append(count)
#     if list2 not in list1:
#         list1.append(list2)
#     i+=1
# print(list1)


# l=[3,4,1,4,9,3,7,5]
# i=1
# while i<len(l):
#     l.pop(i)
#     i+=1
# print(l)
    

# a=[[1,2,3]],[[4,5,6]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         print(a[i][j])
#         j+=1
#     i+=1


# num=[50,4,23,70,56,12,5,10]
# i=0
# less_than_40=0
# more_than_20=0
# while i<len(num):
#     number=num[i]
#     if number<40:
#         less_than_40+=1
#     else:
#         more_than_20+=1
#     i+=1
# print("less 40",less_than_40)
# print("more 20",more_than_20)


# n=["rhutuja","zanu","aonu","ionu"]
# max=n[0]
# for i in n:
#     if i <max:
#         max=i
# print(max)
# i=0
# max=n[i]
# for i in n:
#     if i<max:
#         max=i
# print(max)

# a=[3,5,2,8,9]
# i=0
# max=a[i]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i+=1
# print(max)

# a=[4,5,-9,7,0,-3,-5]
# i=0
# l=[]
# while i<len(a):
#     if a[i]<0:
#         l.append(0)
#     else:
#         l.append(a[i])
#     i+=1
# print(l)


# a=[1,2,3]
# pair=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             a=[a[i],a[j],a[k]]
#             pair.append(a)
#             k+=1
#         j+=1
#     i+=1
# print(pair)

# number=30
# n = [10,11,12,13,14,17,18,19]
# i=0
# a=[]
# while i < len(n):
#     j=4
#     while j < len(n):
#         if n[i]+n[j] == number:
#             a.append([n[i],n[j]]) 
#         j+=1
#     i+=1
# print(a)  


# list1=[1,2,3,4,5,6]
# list2=[2,3,1,0,6,7]
# i=0
# while i<len(list1):
#     if list1[i] not in list2:
#         print(list1[i],end=",")
#     i+=1


# num=int(input("enter the number"))
# i=1
# a=[]
# while i<=10:
#    j=num*i
#    a.append(j)
#    i=i+1
# print(a)

# list2=[[1,2,3,5,6],[7,8,5,3,6],[6,4,9,2,3]]
# i=0
# sum=0
# while i<len(list2):
#     j=0
#     sum1=0
#     a=list2[i][j]
#     while j<len(list2[i]):
#         sum=sum+a
#         j+=1
#     i+=1
# print(list2)


# a=[3,5,8,1,7,2,9,7]
# i=0
# l=[]
# while i<len(a):

#     if i%3==0:
#         a[i:i]=[0]
#     l.append(a[i])
#     i+=1
# print(l)


# sentence = "NavGurukul is an arnative to higher education reducing the barriers of current formal education system"
# # string=sentence.split( ) 
# # print(string)

# a=[]
# b=" "
# for i in sentence:
#     if i==" ":
#         a.append(b)
#         b=" "
#     else:
#         b+=i
# a.append(b)
# print(a)


# a=[10,20,30,40,50]
# b=[100,200,300,400,500]
# k=1
# i=0
# while i<len(a):
#     print(a[i],b[len(b)-k])
#     i+=1
#     k+=1

# a=[1,2,3,4,5,6,8]
# i=0
# l=[]
# k=1
# while i<len(a)-1:
#     l.append([a[i],a[k]])
#     i+=2
#     k+=2
# print(l)

# a=[1,2,3,4,5,6]
# i=0
# l=[]
# while i<len(a)-1:
#     # b=a[i],a[i+1]
#     l.append([a[i],a[i+1]])
#     i+=1
# print(l)


a=[1,2,3]
i=0
pair=[]
while i<len(a):
    j=0
    while j<len(a):
        k=0
        while k<len(a):
            # pair.append([a[i],a[j],a[k]])
            print(a[i],a[j],a[k])
            k+=1
        j+=1
    i+=1


# my_dict = {
#     'a':50, 
#     'b':58, 
#     'c':56,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# a=[]
# for i in range(3):
#     max=0
#     for j in my_dict:
#         if max < my_dict[j]:
#            max = my_dict[j]
#            c=j
#     a.append(my_dict[c])
#     my_dict.pop(c)
# print(a)


# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     s.update(a)
# print(s)

# a=[1,4,6,7,5,6,]
# b={}
# for i in a[::-1]:
#         b={i:b}
# print(b) 

# a=[1,2,3]
# b=['one','two','three']
# d={}
# for i in range(1,len(a)+1):
#     d[i]=b[i-1]
# print(d)


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d1:
#     # print(i)
#     if i in d2:
#         # print(i)
#         d1[i]+=d2[i]
#         d2.update(d1)
#     else:
#         d1[i]=d2[i]
# print(d2)


# l=[[1,2,3],[4,5,6],[7,8,9]]
# sum1=0
# sum2=0
# # l=[]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if j==0:
#             sum1+=l[i][j]
#         if j==1:
#             sum2+=l[i][j]
# print(sum1)
# # print(sum2)

# l.append([sum1,sum2])
# print(l)


# l=[[1,2,3,5],[4,5,6],[7,8,9]]
# i=0
# s=[]
# while i<len(l):
#     j=0
#     sum=0
#     while j<len(l[i])-1:
#         sum+=(l[i][j])
#         j+=1
#     s.append(sum)
#     i+=1
#     print(sum)

# e=input("enter no :")
# if e>="a" and e<="z":
#     print("alphabet")
# elif int(e)>0:
#     print("digit")
# elif e>="a" and e<="z" and int(e)>0:
#     print("other")

# import json
# a={"a":1,"b":2,"c":3}
# print(json.dumps(a))

# a={"a":1,"b":2,"c":3}
# with open ("new_file.json","w") as f:
#     json.dump(a,f,indent=4)

# a='{"a":1,"b":2,"c":3}'
# print(json.loads(a))

# a='{"a":1,"b":2,"c":3}'
# with open ("new_file.json","r") as f:
#     b=json.load(f)
#     print(b)

# a=open("b.txt","x")
# a.close()

# a=open("b1.txt","w")
# a.write("rhutuja patil@20")
# a.close()

# a=open("b3.txt","a")
# a.write("my name is rhutuja\nfghj\npoi90")
# a.close()

# a=open("c1.txt","w")
# a.write("rhutuja patil")
# a.close()

# a=open("c1.txt","r")
# v=a.read()
# print(v)
# a.close()

# a=open("c1.txt","a")
# a.write("yuio\ndfghj\nerdf56\nuio")
# a.close()

# a=open("c4.txt","x")
# a.close()

# a=[1,4,8]
# for i in a:
    # print(i)
    # for j in range(1,9,1):
        # print(j,end=" ")
        # if j not in a:
            # a.append(j)
# print(a)
# a=[4,8,1,7,9,0]
# for i in range(len(a)):
    # for j in range(len(a)-1):
# i=0
# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#             b=a[j]
#             a[j]=a[j+1]
#             a[j+1]=b
#         j+=1
#     i+=1
# print(a)


# for i in 
            
# for i in range(len(q)):
#     q.append([q[i]+1])
# print(q)


# l=[[1,2,3],[4,5,6],[7,8,9]]
# sum1=0
# sum2=0
# sum3=0
# l=[]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if j==0:
#             sum1+=l[i][j]
#         if j==1:
#             sum2+=l[i][j]
#         if j==2:
#             sum3+=l[i][j]
# print(sum1)
# print(sum2)
# print(sum3)

# l=[2,3,[4,6,6],7,[8,6]]
# sum1=0
# for i in range(len(l)):
#     if type(l[i])==list:
#         for j in range(len(l[i])):
        
#             sum1+=l[i][j]
#     else:
#         sum1+=l[i]
# print(sum1)

# a=[[1,2,3,8],[4,5],[7,8,9]]
# sum=0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         sum+=a[i][j]
# print(sum)



# a=[4,6,1,9,0,3,2,7]
# i=0
# l=[]
# while i<len(a)-1:
#     b=[a[i],a[i+1]]
#     l.append(b)
    
#     i+=1
# print(l)










            



