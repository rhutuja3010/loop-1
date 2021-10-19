fibonacci=int(input("enter the number: "))
x=0
y=1
z=0
while z<=fibonacci:
    print(z)
    x=y
    y=z
    z=x+y
    
