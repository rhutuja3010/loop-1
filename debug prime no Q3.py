# i = 2
# num=int(input("enter the number"))
# while (i<num):
#     if (num%i == 0):
#         print(num, 'is not a prime number')
#         break
#     i = i + 1
# else:
#     print(num, 'is a prime number')


i=1
number=int(input("enter the number"))
count = 0
while i <= number:
    if number%i==0:
        count+=1
    i+=1
if count==2:
    print("it is prime number")
else:
    print("it is not prime number")

# str=input("enter a string")
# print(str)
# count={}
# for i in str:
#     if i in count.keys():
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)
