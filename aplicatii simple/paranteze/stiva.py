#STIVA MADE BY andrew.ako96 ON INSTAGRAM


stack=[]
strKey=[]

def push(element):
    global stack
    stack.append(element)

    
def pop():
    global stack
    elm=stack.pop()
    return elm

def printf():
    global stack
    print(stack)
    
def get():
    global stack
    return stack

def lenght():
    global stack
    return len(stack)
    
    
def clear():
    global stack
    stack=[]



















# class stiv:
#     def __init__(self,sim,info):
#         self.sim=sim
#         self.info=info
#         
#     
#     def putInfo (sd):
#         
#           
# py= stiv("3hw","kopana")
# py.pop()
#           
# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
# 
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
# 
# p1 = Person("John", 36)
# p1.myfunc()          