# a=[1,2,3,4,5,[6,7,8]]   #make a flat list.
# b=[]
# i=0
# while i<len(a):
#     if type(a[i]) is list:
#         j=0
#         while j <len(a[i]):
#             b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#     i+=1
# print(b)

# user=int(input("number: "))  # check second number is 3 or not if second number is 3 print yes.
# a=(user//100)%10
# if a==3:
#     print("yes")
# else:
#     print("no")

# a=[1,2,3,4,5,6,7,8,9,10]
# c={}
# for i in a:
#     b={}
#     for j in range(0,i):
#         s=i*5
#         b.update({i:s})
#     # print(b)
#     c.update(b)
# print(c)

# a=[1,2,1,3,4,3,4,3,2,5,2,2,1]
# b={}
# for i in a:
#     d=a.count(i)
#     e=d//2
#     b.update({i:e})
# #     b[i]=d
# # print(b)
# print(b)

# def string(s):
#     upper_case=0
#     lower_case=0
#     for c in s:
#         if c.isupper():
#             upper_case+=1
#         elif c.islower():
#             lower_case+=1

#         else:
#             pass
#     print("original string",s)
#     print("no.of upper case char",upper_case)
#     print("no.of lower case char",lower_case)
# string("The quick Brown Fox")


# def string(string1):
#     upper1=0
#     lower2=0
#     for i in string1:
#         if i.isupper():
#             upper1+=1
#         elif i.islower():
#             lower2+=1
#         else:
#             pass
#     print("no of upper_latter :",upper1)
#     print("no of lower_later :",lower2)
# string("Rhutuja")


# n=int(input("Enter the number: "))
# i=0
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
#     print(sum)

# countewr=0
# while countewr<3:
#     print("inside loop")
#     countewr+=1
# else:
#     print("outside loop")

# i=0
# while i<=5:
#     if i==3:
#         break
#     i+=1
#     print(i)

# for i in "string":
#     if i=="i":
#         break
#     print(i)


# for i in "string":
#     if i=="i":
#         continue
#     print(i)


# for i in range(1,10):
#     print(i)


# a=[1,3,5,7,8,10]
# i=1
# while i<=10:
#     if i not in a:
#         print(i)
#     i+=1


# a=[1,3,5,7,8,10]
# i=1
# b=[]
# c=[]
# for i in a:
#     j=0
#     while j<=10:
#         if j not in a:
#             b.append(j)
#             c.append(b)

#     print(c)
# j+=1


# list=["q","z"]
# num=int(input("enter your number: "))
# i=1
# while i<=num:
#     j=1
#     while j<num:
#         j+=1
#     print( '"' +"q",str(i), '"','"' +"z",str(i),'"')     
#     print()
#     i+=1


# num=int(input("enter the number: "))
# a={}
# for i in range(num,num+1):
#     x=num*i
#     a.update({i:x})
# print(a)

# a={"a":3,"b":5,"c":8,"d":10}
# i=None
# j=-1
# for k in a:
#     if  i is None or i <a[k]:
#         i=a[k]
#         j=k
# print(k)

# d1={"a":100,"b":200,"c":300}
# d2={"a":300,"b":200,"d":400}
# d3={}
# sum=0
# for x in d1:
#     if x in d2:
#         sum=d1[x]+d2[x]
#         d1[x]=sum
#         d2.pop(x)
# d1.update(d2)
# # print(d1)




# list=[5,6,[],3,[],[],9]
# i=0
# a=[]
# while i<len(list):
#     if list[i]!=[]:
#         a.append(list[i])
#     i+=1
# print(a)


# list=[5,6,[],3,[],[],9]
# i=0
# a=[]
# while i<len(list):
#     if  type(list[i])==int:
#         a.append(list[i])
#     i+=1
# print(a)


# list=[["g","f","g"],["i","s"],["b","e","s","t"]]
# a=list[0]+list[1]+list[2]
# b=a
# print(b)
# s = ""
# s = s.join(b)
# print(s)
# _123var=1
# print(_123var)

# list=["subreena"]
# for i in list:
#     a=i[::-1]
# print(a)

# user=int(input("enter a number:"))
# a={}
# b={}
# i=0
# while i<user:
#     name=input("enter ur name: ")
#     age=int(input("enter ur age: "))
#     a[name]=age
#     b[i+1]=a
#     i+=1
# print(b)

# user=int(input("enter a number:"))
# a={}
# b={}
# i=0
# while i<user:
#     name=input("enter ur name: ")
#     age=int(input("enter ur age: "))
#     a[name]=age
#     i+=1
# print(a)


# list=[11,12.9,3,11,"python","js"]
# i=0
# a=[]
# while i<len(list):
#     if type(list[i])==str:
#         # print(list[i])
#         a.append(list[i])
#     i+=1
# print(a)


# user1=int(input("number: "))
# user2=int(input("number: "))
# user3=int(input("number: "))
# if user1>user2:
#     print(user1,"greater")
# elif user2>user3:
#     print(user2,"greater")
# else:
#     print(user3,"graeter")


# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# i=4
# j=0
# while i<len(a):
#     if j==0:
#         a[i]=15
#         j=1
#     else:
#         a[i]=20
#         j=0
#     i+=5
# print(a)


# a=[[1,2,3,4],[5,6,7,8],[8,9,10]]
# list=[]
# i=0
# sum=0
# sum1=0
# sum2=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if j==0:
#             sum=sum+a[i][j]
#         elif j==1:
#             sum1=sum1+a[i][j]
#         elif j==2:
#             sum2=sum2+a[i][j]
#         elif j==3:
#             list.append(a[i][j])
#         j+=1
#     i+=1
# list.append(sum)
# list.append(sum1)
# list.append(sum2)
# print(list)


# i=100
# sum=0
# while i>0:
#     sum=sum+i
#     i-=1
# print(sum)


# list=["a","b","c","d","a","c","d","e","f","a","b"]
# i=0
# o=0
# while i<len(list):
#     if list[0]==list[i]:
#         k=(i)
#     elif list[1]==list[i]:
#         l=(i)
#     elif list[2]==list[i]:
#         m=(i)
#     elif list[3]==list[i]:
#         n=(i)
#     elif list[7]==list[i]:
#         o=(i)
#     elif list[8]==list[i]:
#         p=(i)
#     i+=1
# print(list[0],":",k,list[1],":",l,list[2],":",m,list[3],":",n,list[7],":",o,list[8],":",p)

# a=[1,2,3,4,5,6,7,8,9,10]
# c={}
# for i in a:
#     b={}
#     for j in range(0,i):
#         s=i*5
#         b.update({i:s})
#     c.update(b)
# print(c)