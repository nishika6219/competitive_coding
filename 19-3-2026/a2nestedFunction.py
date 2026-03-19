#nested function

def outerfunction():
    print("this is my outer function") #2nd
    def innerfunction():
        print("inner function") 
    innerfunction()#3rd
outerfunction()#1st
