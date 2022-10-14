pas=False
print("Aplicatie pentru verificarea pozitiei unui punct")

while(True):
    x = float(input("Alegeti o valoare pentru x :\n"))
    y = float(input("Alegeti o valoare pentru y :\n"))
            
    if(x>0 and y>0):
            print("Punctul de coordonate",x,"si",y,"se afla in cadranul 1")
            
    elif(x>0 and y<0):
            print("Punctul de coordonate",x,"si",y,"se afla in cadranul 4")
             
    elif(x<0 and y>0):
            print("Punctul de coordonate",x,"si",y,"se afla in cadranul 2")
             
    elif(x<0 and y<0):
            print("Punctul de coordonate",x,"si",y,"se afla in cadranul 3")
    exit=input("Daca doriti sa incheiati programul tastati orice\n")
    if exit != "":
         break
              
             