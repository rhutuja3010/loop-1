num=int(input("enter any number")) 
temp=num
sum=0
while temp!=0:
    remd=temp%10
    sum=sum+remd
    temp=int(temp//10)
if num%sum==0:
    print(num,"is a harshad number")  
else:
    print(num,"is not a harshad number")       