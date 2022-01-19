 # user log in attempts
 
for i in range (0,4):
	 if i<4:
	 	username=str(input("enter username"))
	 	password=int(input("enter password"))
	 	if username=='vineethreddy' and password==123123:
	 		print("your log in  successfully completed")
	 		break
	 	else:
	 		print('you have' ,3-i, 'attempts')