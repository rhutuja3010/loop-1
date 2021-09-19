geuss_number=int(input("enter the geuss number"))
i=1
while i<5:
    if geuss_number == 5:
        print("congratulation, your geuss is correct")
        break
    else: 
        print("sorry, your guss is wrong")   
    agin_geuss_number=int(input("enter the geuss number"))
    if agin_geuss_number == 5:
        print("congratulation, your geuss is correct")
        break
    i=i+1
        
        
    
 