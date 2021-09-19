i=1
sum=0
while i<=11:
    num=int(input("enter the weight:"))
    i=i+1
    sum=sum+num
print("sum is",sum)
average=sum/11 
print("average",average)  
if average%5==0:
    print("Divisible by 5")
else:
    print("Not divisible")