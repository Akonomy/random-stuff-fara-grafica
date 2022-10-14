#calculare factorial
def factorialFunction(factorial):
    y=1
    for x in range(int(factorial+1)):
        if x!=0:
         y=y*x
    return y
        
   #functia propriu-zisa     
while(True):
    n = int(input("Alegeti o valoare pentru n :\n"))
    k = int(input("Alegeti o valoare pentru k :\n"))
    if n>0 and k>0:
       nFactorial = factorialFunction(n)
      # print(nFactorial)
       kFactorial = factorialFunction(k)
      # print(kFactorial)
       nk=n-k
      # print(nk)
       nkFactorial = factorialFunction(nk)
      # print(nkFactorial)
       
       result=nFactorial/(kFactorial*nkFactorial)
       print("Combinari de", n ,"luate cate", k," sunt ",result)
   
       exit=input("Daca doriti sa incheiati programul tastati orice\n")
    if exit != "":
         break
              

