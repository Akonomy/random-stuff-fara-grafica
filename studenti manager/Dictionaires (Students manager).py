from random import*
#functia de decodificare a ceea ce se da de la tastatura
def decodeS(string):
    string+=" "
    Id=""
    Name=""
    Nota=""
    Notes=[]
    pas=0
    try:
        for x in string:
          if pas==0:
              if x==",":
                  pas+=1
              else:
                Id+=x
          elif pas ==1:
              if x==",":
                  pas+=1
              else:
                Name+=x

          elif pas ==2:
              if x==" ":
                  try:
                      Notes.append(float(Nota))
                      Nota=""
                  except:
                      pass
              else:
                  if x.isnumeric() or x==".":
                      Nota+=x
                      
              
                  
        return[Id,Name,Notes]
    
    
    except:
        print("Ceva nu a mers bine la decodificare")
# a=decodeS("465,dysg sd,7 43 2.8 9")
# print(a)
#Pana aici e functia de decodificare a oricarui string de la tastatura
        
#meniu principal        
menu={
    "1":"Load info Studenti(tastatura)",
    "2":"Afisare studenti",
    "3":"Afisare note",
    "4":"Afisare studenti+note",
    "5":"Cauta student dupa nume",
    "6":"Afisare studenti primovati",
    "7":"Info author",
    "8":"Exit",
    "9":"Salvare in fisier txt",
    "10":"Load info Studenti(fisier)",
    "11":"Incarcare studenti random din baza de date",
    }
#dictionarul sursa unde se vor stoca datele despre studenti
student={
    "ID":["   Nume\t","   Notes  "],
    }
#info 
infoAutor={
#   "INFO":"AUTOR PROGRAM",
    "Nume Prenume":"Spac Andrei",
    "Specializare":"AIA",
    "An":1,
    "Grupa":"3211B",
    "Email":"andrei.spac@student.usv.ro",
    }
#print("ID  ",student["ID"][0],"    ",student["ID"][1])
#print("ID  ",student["ID"][1])
#print("ID  ",student["ID"][0])

#print menu
###########################################################

#functie de afisare a meniului principal
def print_menu():
    print("\n\n  \--------MENIU---------/" )
    for x in menu.keys():
        print(x, "->",menu[x])

#functie de generare studenti random(NEINCLUSA IN TEMA)
def randStudent():
            keyPas=input("Doriti sa generati fisier studenti.txt cu valori predefinite?\n Enter for yes/ n for no")
            if keyPas=="":
                maxIn=input("Cati studenti doriti sa adaugati?(maxim 34)\n")
                if maxIn.isnumeric:
                    if int(maxIn)<35 and int(maxIn)>0:
                        pass
                    else:
                        maxIn=20
                else:
                    maxIn=20
                try:
                   # f=open("studenti.txt","wt")
                   #necesita un fisier sursa
                    name=open("names.txt","rt")
                    
                    for x in range(int(maxIn)):
                        qpass=0
                        strNotes=[]
                        strName=''
                        k=0
                        randA=randint(1,1)
                        while k<(randA):
                            strNameTemp=str(name.readline())
                            k+=1    
                        for l in strNameTemp:
                            if l=="\n" :
                                pass
                            else:
                                strName+=l
                        Id=str("B"+str(x)+"c")
                        for i in range(4):
                            strNotes.append(randint(2,10))    
                        info=[strName,strNotes]
                        if Id==" ":
                            pass
                        else:
                            student[Id]=info
                    # print("eroare")
                    #f.close()
                    name.close()
                    data="{},{},\b{} \n"
                    f=open("studenti.txt","wt")
                    for x in student.keys():
                         if x!="ID" and x!="  ":
                             f.write(data.format(x,student[x][0],student[x][1]))           
                    f.close()
                    print("Fisierul s-a salvat cu succes")
                except:
                    print("Nereusit, ne pare rau ")



############################################################



#loop de afisare a meniului principal si preluare optiuni
while(True):
    print_menu()
    option=input("Alegeti o optiune\n")
    
    if option == "1":
        amax=input("Cati studenti doriti sa adaugati?\n")
        print("example: bw2,Name Prename,10 8 9 \n where bw2 = id")
        for a in range(int(amax)):
            strKey=input("Va rugam sa introduceti info student \n")
            #se apeleaza functia decode
            verify=decodeS(strKey)
            #se atribuie valorile date de functie
            Id=verify[0]
            info=[verify[1],verify[2]]
            student[Id]=info
    elif option =="2":
        #afisare id plus primul lucru din lista atribuita id-ului 
        for x in student.keys():
            print(x, "   ",student[x][0])
    elif option =="3":
        for x in student.keys():
            print(x, "   ",student[x][1])
    elif option =="4":
        for x in student.keys():
            print(x, "   ",student[x][0],"   ",student[x][1])
    elif option =="5":
        Ufind=True
        search=input("Introduceti nume student\n")
        for x in student.keys():
            if student[x][0]==search:
                print(x, "   ",student[x][0],"   ",student[x][1])
                Ufind=False
        if Ufind:
            print("Nu s-a gasit studentul\n")
    elif option =="6":
        print("ID     Nume      Media")
        #doua variabile neincluse in tema)
        nepromovat=0
        promovat=0
        for x in student.keys():
            try:
                if sum(student[x][1])/len(student[x][1])>=5:
                    print(x, "   ",student[x][0],"    ",sum(student[x][1])/len(student[x][1]))
                    promovat+=1
                else:
                    nepromovat+=1            
            
            except:
                pass
        print("Studenti nepromovati  ",nepromovat,"\nStudenti promovati  ",promovat)
    elif option =="7":
        for x in infoAutor.keys():
            print(x, ">>>",infoAutor[x])
    elif option =="8":
        print("Se inchide programul... \n")
        break
    
    
    #NEINCLUSE IN TEMA PENTRU A VEDEA CUM SE POATE FACE O CITIRE DIN FISIER 
    elif option =="9":
        try:
            #deoarece am folosit wt si nu at
            #mai multe info despre gestionarea fisierelor in python gasiti aici
            #https://www.w3schools.com/python/python_file_handling.asp
         run=input("Salvarea fisierului presupune stergerea informatiilor anterioare\n Doriti sa continuati?\n\nEnter for yes/ n for no\n")
         if run=="":
             data="{},{},{} \n"
             f=open("studenti.txt","wt")
             for x in student.keys():
                 if x!="ID" and x!="  ":
                     f.write(data.format(x,student[x][0],student[x][1]))           
             f.close()
             print("Fisierul s-a salvat cu succes")
         else:
             print("Salvarea fisierului nu a reusit(anulata)")
        except:
            print("Salvarea fisierului nu a reusit din diverse motive")
      #citirea din fisier, atentie in cazul care nu exista fisierul      
    elif option =="10":
        try:
            #salt=True
            f=open("studenti.txt","rt")
            for x in range(30):
               # if salt:
               #     salt=False
               #     f.readline()
               # else:
                    strFile=str(f.readline())
                    verify=decodeS(strFile)
                    Id=verify[0]
                    info=[verify[1],verify[2]]
                    if Id==" ":
                        pass
                    else:
                         student[Id]=info
                   # print("eroare")
            f.close()
            print("Citirea fisierului s-a efectuat cu succes")
        except:
            print("Nu s-a putut deschide studenti.txt\n>>Make sure the file is in same folder as program\n")
            randStudent()

            
                
    elif option=="11":
        randStudent()
        #in cazul care optiunea nu a fost validata printeaza invalid
    else:
        print("Invalid")
        
        #Nu uitati sa inchideti mereu fisierul dupa ce il deschideti pentru a nu avea probleme:))
        #ctrl+3 pe un text selectat pentru a trece tot in comentarii Alt+4(nu F4) pentru scoatere din com
        #ctrl+space pentru completare automata sau dubluclick tab
        #pentru a importa module
        # from math import sqrt    >>> importa doar functia sqrt din modulul math
        # from math import*        >>> importa toate functiile din modulul math
        # Utilizeaza acest fisier doar pentru inspiratie te rog :))
        
        
        
    

