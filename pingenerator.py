from random import randrange

done = False

def pingenerator():
    print("Generating number...")
    n1 = randrange(1,10)
    n2 = randrange(1,10)
    n3 = randrange(1,10)
    n4 = randrange(1,10)
    return print("\n---------\n",n1,n2,n3,n4,"\n---------\n")

def message():
    uput = "0"
    uput = int(input("Is this a good number? y/n: "),36)
    if uput == 34:
        done == True
    elif uput == 24:
        done == False
    else:
        print("Command not understood. Generating new number")

while done == False:
    pingenerator()
    message()
print("Thank you for using pingenerator!\nYour new pin number is: ",n1,n2,n3,n4)

    
