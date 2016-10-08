from hashlib import *

new = input("Press 1 to login or 0 to exit. ")
tel = {}
x = 1

if new=="1":
    username = input("Username: ")
    password = input("Password: ")

    if username in tel:
        while(x>0):
            username = input("Username: ")
            password = input("Password: ")
            if sha512(password.encode('utf-8')).hexdigest() == tel[username]:
                print("Congrats! You're in.")
                x = 0
            else:
                print("Sorry, try again!")
                x = x+1
                
    elif username not in tel:
        print("This account does not exist yet. ")
        newP = input("Please type in a new password. ")
        tel[username] = sha512(newP.encode('utf-8')).hexdigest()

        while(x>0):
            username = input("Username: ")
            password = input("Password: ")
            
            if sha512(password.encode('utf-8')).hexdigest() == tel[username]:
                print("Congrats! You're in.")
                x = 0
            else:
                print("Sorry, try again!")
                x = x+1
                
elif new=="0":
    print("Okay, bye-bye!")
    exit()
##sha256(‘MYSTRING’.encode(‘utf-8’)).hexdigest() 
# The above will give you a hash of MYSTRING
