#calculator 
print("welcome to the calculator")    
num_1=int(input("enter the first calculated number : "))    #first calculation number 
operator=input("enter the opeperator, + - / * %    :  ")    # which type of operator
num_2=int(input("enter the second calculated number    :  "))  # second calculation number
if operator =="+":
    print("total is",num_1+num_2) # addition
elif operator =="-":
    print("total is",num_1-num_2)  #subtrction
elif operator =="/":
    print("total is",num_1/num_2)   #divide
elif operator =="*":
    print("total is",num_1*num_2)   #multiplication
elif operator =="%":
    print("total is",num_1%num_2)    #modules
else:
    print("please to check the your operator ")