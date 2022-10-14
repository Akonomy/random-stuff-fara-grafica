class stack:
    def __init__ (self,elm="s1"):
        self.elm=[]
    def push(self,o):
        self.elm.append(o)
    def printf(self,elm="s1"):
        print(self.elm)
    def pop(self,elm="s1"):
        r=self.elm.pop()
        return r
    def leng(self,elm="s1"):
        a=len(self.elm)
        return a
    #print(stack)
    
#     
# s1=stack()
# 
# print(s1)
# s1.push(8)
# s1.printf()
# s1.push(6)
# s1.printf()
# s2=stack()
# s1.pop()
# s2.printf()
# s2.push(6)
# s1.printf()
# s2.printf()
# 

def hei(name="Ak"):
    print(name)
    
