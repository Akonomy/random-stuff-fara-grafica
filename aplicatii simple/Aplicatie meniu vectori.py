vector=["NULL",]
#functie de determinare a minimului
def detValoareMinima(vector):
    minim0=vector[0]
    for x in range(len(vector)-1):
        a=minim0
        if a<vector[x+1]:
            minim0=a
        else:
         minim0=vector[x+1]
        #print(x)        
    return minim0

#functie de determinare a maximului
def detValoareMaxima(vector):
    maxim0=vector[0]
    for x in range(len(vector)-1):
        a=maxim0
        if a>vector[x+1]:
            maxim0=a
        else:
                maxim0=vector[x+1]
        #print(x)        
    return maxim0
def cautareElement(vector):
    pas=False
    cautat=input("Ce element doriti sa cautati?\n")
    for x in vector:
        if x == cautat:
            pas=True
    if pas:
        print("S-a gasit elementul",cautat,"in lista")
    else:
        print("Nu s-a gasit elementul",cautat,"in lista")
            
            



#functie de citire si afisare interval ++ lungime :))
def citireInterval(vector):
    a=int(input("De la al catelea element doriti sa afisati elementele?\n"))
    b=int(input("Pana la al catelea element doriti sa afisati elementele?\n"))    
    print("vectorul este ",vector[a:b],"\n","lungime:",len(vector[a:b]))
    
def addElement(vector):
    add=input("Ce element doriti sa adaugati?\n")
    where=int(input("Unde doriti sa-l adugati? (index location)\n"))
    vector.insert(where,add)
    return vector


def sortList(vector):
    vector.sort()
    return vector





menu={
    "c":"citire vector",
    "a":"afisare vector",
    "m":"minim from vector",
    "M":"maxim from vector",
    "f":"cautare element in vector",
    "g":"numararea elementelor care apartin intervalului [a,b)",
    "i":"inserarea unui element nou",
    "s":"sortarea vectorului a->z",
    "x":"exit"
    }
#funtie ca sa afiseze frumos meniul ;))
def print_menu():
    print("\--------MENIU---------/" )
    for x in menu.keys():
        print(x, "->",menu[x])
        #facem un while care v-a printa meniul apoi va cere o optiune



while(True):
 print_menu()
 option = input("Enter the option, please \n")
 
 if option == "c":
     #functie de creare a listei
  nrElemente=int(input("Cate elemente doriti sa adaugati?\n"))
               
  for x in range(nrElemente):
   elmAdaugat=input("Add an element\n->  ")
   vector.append(elmAdaugat)
  vector.remove("NULL")
  
 elif option == "a":
  print(vector)
  
 elif option == "m":
    temp = detValoareMinima(vector)
    print(temp)
 elif option == "M":
    temp = detValoareMaxima(vector)
    print(temp)
 elif option == "f":
     cautareElement(vector)
     
 elif option == "g":
     citireInterval(vector)
     
 elif option == "i":
     addElement(vector)
     
 elif option == "s":
     sortList(vector)
     
 elif option == "x":
     break
    
 else:
  print("Nu avem aceasta optiune :((")
     
#      
# #verificare functii
# print(vector)
# vector=addElement(vector)
# h=detValoareMinima(vector)
# print(h)
# h=detValoareMaxima(vector)
# print(h)
# cautareElement(vector)
# citireInterval(vector)
#               