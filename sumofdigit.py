number=int(input("enter the number: "))
sum=0
modulus=0
while number!=0:
    modulus=number%10
    sum+=modulus
    number//=10
print(sum)