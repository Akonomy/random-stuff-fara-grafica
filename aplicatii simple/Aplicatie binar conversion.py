#functia de transformare din decimal in binar

def binaryFunction(value):
    pas=0
    result=["go",]
    a=value
    while(True):
     binary=a%2
     result.append(int(binary))
     if pas==1:
         break
     a=a/2
     if int(a)<float(a):
        a=a-0.5
     if a<=1:
         pas=1
    result.remove("go")
    return result


# functia de rulare 
while(True):
 inputValue=int(input("Va rugam sa introduceti numarul de transformat\n"))
 y=binaryFunction(inputValue)
 y.reverse()
 
 print("binar form of ",inputValue,":\n--------\n")
 
 for i in range(len(y)):
    print(y[i])
    
    
 exit=input("Daca doriti sa incheiati programul tastati orice\n")
 if exit != "":
  break

