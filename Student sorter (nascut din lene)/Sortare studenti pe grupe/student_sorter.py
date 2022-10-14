#sortare grupe


def openFile( file ):
    
    f=open(file,"rt")




    lista=[]


    for x in f:
       # print(x)
        
        a=x.strip("\n")

        a=a.split()
        nr=len(a)
        if nr != 0:
            #print(a);
            b=a[len(a)-1]
            #print(b)
            lista.append([b,x])

    f.close()
    
    return lista
openFile("calculatoare.py")
def procesareLista(lista):
    lista.sort()
    listaGrupe={}
    grupe=[]
    grupe=set(grupe)
    for y in lista:
        grupe.add(y[0])
#     print(grupe);    
    for x in lista:
            
        for indicator in grupe:
            if x[0]==indicator:
                if indicator in listaGrupe:
                    listaGrupe[indicator].append(x[1])
                else:
                    listaGrupe[indicator]=[]
                    listaGrupe[indicator].append(x[1])
    return listaGrupe

def function (listaB):
    listaFinala=[]
    listaB.sort()
    for y in listaB:
        temp=y.split()
        #print(temp)
        z=temp[1]+" "+temp[2]+" "+temp[3]
        
        listaFinala.append(z)
        
    listaFinala.sort()
    return listaFinala
        
#     for x in range(len(listaB)):
#         a=listaB[x]
#         if a[2:3]==' ':
#             listaB[x]=a[3:len(a)-1]
#         else:
#             listaB[x]=a[2:len(a)-1]
#         
# 
#     listaB.sort()    
# 
#     for x in range(len(listaB)):
#         a=listaB[x].split()
#         listaB[x]=a[0]+" "+a[2]
#         
#     for x in listaB:
#         listaFinala.append(x)
#         print(x);
#     print("\n\n");    
#     return listaFinala    
    
    
# function(listaGrupe["a"]);
# 
# print("\n\n");
# 
# function(listaGrupe["b"]);



  
        
        
        
    
