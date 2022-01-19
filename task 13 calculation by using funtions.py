#calculator using functions

def add(a,b):
    return a+b


def add(a,b):
    return a+b

def sub(a,b):
    return a-b


def mul(a,b):
    return a*b


def div(a,b):
    return a/b


def mod(a,b):
    return a%b


name=input("enter your name:  ")
print("hello", name)

while True:
    operator=input("enter the opeperator, + , - , / , * ,  %    :  ")    # which type of operator
    if operator in ('+','-','*','/','%'):
        a=float(input("enter the first calculated number : "))    #first calculation number 
        b=float(input("enter the second calculated number    :  "))  # second calculation number


    if operator =="+":               #addition
        a=add(a,b)
        print(a)
    elif operator =="-":              #subtrctiona
        b=sub(a,b)
        print(b)                
    elif operator =="/":              #division
         c=div(a,b)
         print(c)   
    elif operator =="*":               #multiplication
        d=mul(a,b)
        print(d)   
    elif operator =="%":                #modules
       e=mod(a,b)
       print(e)

    Another_calculation=input("If you want to go next calculation yes and no for exit ")
    if Another_calculation=="no":
        break
    else:
        print("please to check the your operator ")
