

password=input("enter the Strong password :")
if len(password)>=6 and len(password)<=16:
    if  "$" in password or "@"in password:
        if "2" in password or  "8" in password:
            if "A" in password or "Z" in password:
                print("this is strong password")
            else:
                print("this is weak password")
        else:
            print("wrong")
    else:
        print("invalid")
else:
    ("no")

