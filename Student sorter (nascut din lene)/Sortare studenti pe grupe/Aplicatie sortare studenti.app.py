#menu app
from student_sorter import*



menu={
    "\n1":"Alegeti fisierul cu studenti",
    "2":"Procesarea studentilor pe grupe",
    "3":"Afisarea grupelor",
    "4":"Afisarea studentilor din grupa:",
    "5":"Exit"
    
    }

while True :
    
    for x in menu.keys():
        print(x,"===", menu[x]);
    
    optiune=input("\nAlegeti va rog : \n")
    
    if optiune == "1":
        fisier=input("introduceti numele fisierului(enter for default): \n")
        if fisier=="":
            try:
                lista=openFile("stud.py")
                print ("\033[1;32m fisierul a fost deschis \n ");
                print("\033[1;0m");
            except:
                print("\033[93;31m Nu s-a gasit fisierul default 'stud.py' \033[0;0m");
        else:
            try:
                lista=openFile(fisier)
                print ("\033[1;32m fisierul a fost deschis " );
                print("\033[1;0m");
            except:
                print("\033[93;31;47m Nu s-a gasit fisierul ", fisier, " in folder \033[0;0m");
        
        
    elif optiune == "2":
        try:
            listaGrupe=procesareLista(lista)
            print("\033[1;32m procesarea s-a facut cu succes\n");
            print("\033[1;0m");
        except:
            print("\033[93;31;47m ceva nu a mers bine , ati incarcat fisierul?\033[0;0m");

    elif optiune == "3":
        try:
            
            text=""
            for x in listaGrupe.keys():
                text+="  "+str(x)
            print(text);    
        except:
            print("\033[93;31;47m Nu s-au gasit grupe de afisat\033[0;0m\n ");
            
    elif optiune == "4":
        try:
            indicator=input("alegeti grupa va rog :\n")
            lista=function(listaGrupe[indicator]);
            
            print("Studentii din grupa " ,indicator,"\n");
            for x in lista:
                print(x)
                
        except:
            print("S-au pierdut studentii pe drum, stiti unde sa ii gasim? \n\n"
                  "asigurati-va ca fisierul a fost incarcat si nu contine diacritice");
            
            
            
        
    
    elif optiune == "5":
        break;