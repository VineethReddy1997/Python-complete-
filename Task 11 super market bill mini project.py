from datetime import datetime


Customer_name=input("Enter your name : ")

lists="""
oil                 120rs/kg
onions               50rs/kg
sugar                40rs/kg
salt                 20rs/kg
bread                20rs/1piece
chakragold          200rs/kg
colgate             100rs/100grams
tooth brush         100rs/3pieces
soaps               100rs/5pieces
red chilli powder   200rs/kg
turmeric powder     200rs/kg
almonds             500rs/kg
badam               500rs/kg
boost                40rs/kg
horliks             500rs/kg
"""

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]


items={'oil':120,
'onions':50,
'sugar':40,
'salt':20,
'bread':20,
'chakragold':200,
'colgate':100,
'tooth brush':100,
'soaps':100,
'red chilli powder':200,
'turmeric powder':200,
'almonds':500,
'badam':500,
'boost':40,
'horliks':500}

select=int(input("For list of items press 1 : "))
if select==1:
    print(lists)
for k in range(len(items)):
    inp=int(input('If you want buy press 1 or press 2  for exist:'))
    if inp==2:
        break
    if inp==1:
        item=input('Enter your items: ')
        quantity=int(input('Enter quantity: '))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*3)/100
            finalamount=gst+totalprice
        else:
            print('your enterterd item is not there in store')

    else:
        print('your slecting number is wrong')
    inp=input('can i bill your items YES or NO :   ')  
    if inp=="YES":
        pass
        if finalamount!=0:
            
            print(20*"=","VIneETh ReDDy DiGiTaL SuPeR MaRkEt",20*"=")
            print(28*" ","PALVANCHA(M),B.KOTHAGUDEM(D)" )
            print("Name:",Customer_name,30*" ", "DATE:",datetime.now())
            print(75*"_")
            print("S.no",8*" ","Items",8*" ","Quantity",3*" ","Price")
            for k in range(len(pricelist)):
                print(k,5*' ',5*' ',ilist[k],10*' ',qlist[k],10*' ',plist[k])
            print(75*"_")
            print(50*" ","ItemsPrice :","Rs",totalprice)
            print(75*"-")
            print(51*" " ,"Gst Amount  :","Rs",gst)
            print(75*"-")
            print(50*" ","TotalAmount:","Rs",finalamount)
            print(75*"_")
            print(50*" ","THANK YOU FOR VISITING")
            print(75*"_")
 
                
 