from stiva import*
import stiva

string="()()"
#Coming soon
#verificare orice tip de paranteze
def dec (strKey):
    pushed=False
    end=False
    for x in strKey:
        if x=="(":
            stiva.push(x)
            pushed=True
        elif x==")":
            try:
                stiva.pop()
            except:
                end=True

    if stiva.lenght()==0 and pushed:
        if not end:
            print("Parantezele sunt inchise corect")
            pushed=False
        else:
            print("incorect.")

            
    else:
        print(" incorect.")
    stiva.clear()
while string!="":        
    string=input("Introduceti parantezele  \n")        
    dec(string)        
