# n = int(input("enter any number")) 
# temp = n
# sum = 0
# while temp != 0:
#     r = temp%10
#     sum = sum+r
#     temp = temp//10
# if n % sum == 0:
#     print(n,"is a harshad number")  
# else:
#     print(n,"is not a harshad number") 

n=int(input("enter the number"))
temp=n
sum=0
while temp!=0:
    r=temp%10
    sum=sum+r
    temp=temp//10
if n%sum==0:
    print(n,"it is harshad number")  
else:
    print(n,"not")    