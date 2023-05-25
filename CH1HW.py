import random

secret = random.randint(0,500)
name = input("Hello, what's your name?")
guess = 0
  
while guess != str(quit):
    guess = (input("Hi "+name+ ", guess a number between 0 - 500"))
    
    if guess == str("quit"):
        break
        
    if int(guess) == secret:
        print("Correct " +name+ ",That's the right number")
        break
 
    elif secret - int(guess) <= 10 >= int(guess) - secret:
        print("You are getting close, " +name+ ".")
 
    elif int(guess) > secret:
        print("Your guess is too high, " +name+".")
           
    elif int(guess) < secret:
        print("Your guess is too low, " +name+".")
        
        
print("Game over")




