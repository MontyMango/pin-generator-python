from random import randint

class pingenerator():
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.n4 = 0
        self.uput = 0
        
    def shownumber(self):
        self.n1 = randint(1,9)
        self.n2 = randint(1,9)
        self.n3 = randint(1,9)
        self.n4 = randint(1,9)
        print("\n---------\n",self.n1,self.n2,self.n3,self.n4,"\n---------\n")
        self.message()

    def message(self):
        self.uput = input("Is this a good number? y/n: ")
        if self.uput == "y":
            print("\nThank you for using pingenerator!",
                "\nYour new pin number is: ", self.n1,self.n2,self.n3,self.n4)
        elif self.uput == "n":
            self.shownumber()
        else:
            print("Command not understood. Generating new number")
            self.shownumber()

p = pingenerator()
p.shownumber()

    
