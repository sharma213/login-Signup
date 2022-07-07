def strong_password(password):
    digit='0123456789'
    capital_alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_alphabet='abcdefghijklmnopqrstuvwxyz'
    special_char='@#$_'
    sum=0
    a=0
    x=0
    y=0
    z=0
    if len(password)>6 or len(password)<=16:
        for i in range(len(password)):
            if password[i] in digit:
                x=1
            elif password[i] in capital_alphabet:
                y=1
            elif password[i] in small_alphabet:
                z=1
            elif password[i] in special_char:
                a=1
        sum=x+y+z+a
        if sum<4:
            print("password should have atleast one capital,one small,one special character and one digit ")
        else:
            print("strong password ")
password=input("enter the password ")
strong_password(password)


