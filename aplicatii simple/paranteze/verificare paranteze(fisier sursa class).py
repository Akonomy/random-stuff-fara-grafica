string="()()"
from stack  import*
#Coming soon
#verificare orice tip de paranteze
#full version 
def dec (strKey):
    deschis0=stack()
    deschis1=stack()
    deschis2=stack()
    caracter=stack()
    incorect=[0,0,0]
    pushed=[0,0,0]
    for x in strKey:
        if x=="(":
            deschis0.push(x)
            pushed[0]=1
        elif x==")":
            try:
                deschis0.pop()
            except:
                incorect[0]+=1
        if x=="[":
            deschis1.push(x)
            pushed[1]=1
        elif x=="]":
            try:
                deschis1.pop()
            except:
                incorect[1]+=1

        if x=="{":
            deschis2.push(x)
            pushed[2]=1
        elif x=="}":
            try:
                deschis2.pop()
            except:
                incorect[2]+=1
        else:
            caracter.push(x)
    if incorect!=[0,0,0]:        
        if incorect[0]>0:
            print("Incorect for ( ",incorect[0]," )\n")
            incorect[0]=0
        elif incorect[0]==0:
            print("Paranteze")
        if incorect[1]>0:
            print("Incorect for [ ",incorect[1]," ]\n")
            incorect[1]=0
        if incorect[2]>0:
            print("Incorect for { ",incorect[2]," }\n")
            incorect[2]=0
            
    elif True:
            
        if pushed[0]==1:        
            if deschis0.leng()==0 and pushed[0]==1:
                print("parantezele rotunde sunt inchise corect\n")
                pushed[0]=0
            else :
                print("parantezele rotunde sunt inchise incorect\n")
        if pushed[1]==1:    
            if deschis1.leng()==0 and pushed[1]==1:
                print("parantezele patrate sunt inchise corect\n")
                pushed[1]=0
            else :
                print("parantezele patrate sunt inchise incorect\n")
        if pushed[2]==1:    
            if deschis2.leng()==0 and pushed[2]==1:
                print("acoladele sunt inchise corect\n")
                pushed[2]=0
            else :
                print("acoladele sunt inchise incorect\n")


while string!="":        
    string=input("Introduceti parantezele  \n")        
    dec(string)        
