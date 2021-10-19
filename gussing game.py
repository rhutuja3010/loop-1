guess_number = int(input("enter the guess number: "))
i=1
while i < 3:
    if guess_number == 5:
        print("congratulation, your guess is correct")
        break
    else: 
        print("sorry, your guess is wrong")   
    again_guess_number=int(input("enter the geuss number"))
    if again_guess_number == 5:
        print("congratulation, your geuss is correct")
        break
    i+=1
        
        
    
 