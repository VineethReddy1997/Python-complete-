# NUMBER GUESSING GAME
print("Hi welcome to the game guessing number")

print("please login  to game with your name")

a=input("Enter your name:")

print(''' Game rule - we will hide 1 to 9 numbers if you select any one number in lessthanequals to three times chances,
 You guess a correct number you are the winner in game and you will get 1000 rupees''')

print("lets start the game")
print('please select one number in 0 to 9')

winning_number=[7,9,3]
lossing_number=[1,2,4,5,6,8,]
for i in range(0,3):
    guess_number=int(input("enter the number:"))
    if guess_number in winning_number:
        print("hello friend you are a winner and you will get 1000 rupees")
        print("Thank you")
        break
    else:
        if guess_number in lossing_number:
            print("chances left",2-i)
            print(" hello friend , you are loss this game better luck next time ")
            

        
        
            
        
    
      
     
        
        
