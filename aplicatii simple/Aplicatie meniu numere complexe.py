# pare=0
# impare=0
# minimSir=0
# maximSir=0
# sir=["go",]
# print("PROGRAM PYTHON 5) \n\n---------------------------\n\n")
# maxim=input("Cate elemente doriti sa adaugati?\n")
# for i in range(int(maxim)):
#     i+=1
#     verify=input("Add element:\n")
#     sir.append(int(verify))
#     if "go" in sir:
#      sir.remove("go")
# print(sir)
#  
# for x in sir:                              
#     if x%2==0:
#         print(x ,"este par")
#     elif x%2!=0:
#             print(x,"este impar")
#             
# #verificare valoare minima
#             
# for x in sir:
#     
#             
#             
#

#----------------------------------------------
exit=0
pas=False
# facem un dictionar unde atribuim strings fiecarei operatii
menu={
    "C":"Citire numere complexe",
    "+":"Aduna numerele",
    "-":"scadere",
    "/":"impartire",
    "x":"iesire din program"
    }
#funtie ca sa afiseze frumos meniul ;))
def print_menu():
    print("\--------MENIU---------/" )
    for x in menu.keys():
        print(x, "->",menu[x])
        #facem un while care v-a printa meniul apoi va cere o optiune
while(exit==0):
 print_menu()
 option = input("Enter the option, please \n")
 if option == "C":
     n1=complex(input("Introduceti un numar complex\n"))
     n2=complex(input("Inca unul sa putem face operatii :))\n"))
     pas=True
 elif option == "+":
     if pas:
         result=n1+n2
         print(n1,"+",n2,"=",result)
     else:
         print("Nu avem ce aduna")
         
 elif option == "-":
     if pas:
         result=n1-n2
         print(n1,"-",n2,"=",result)
     else:
         print("Nu avem ce scadea")
         
 elif option == "/":
     if pas:
         result=n1/n2
         print(n1,"/",n2,"=",result)
     else:
         print("Nu avem ce imparti")
         
 elif option == "*":
     if pas:
         result=n1*n2
         print(n1,"*",n2,"=",result)
     else:
         print("Nu avem ce imulti")
         
 elif option == "x":
     print("Va multumim ca ati utilizat programul nostru")
     break
     
 else:
     print("Nu avem aceasta optiune momentan :(")
     
     #------------------------------------------------------
     
     
     