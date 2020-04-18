import random

game_category = input("Choose one of the three categories; Easy, Medium and hard: ").lower()
easy = 'easy'
medium = 'medium'
hard = 'hard'
chances = 0
chances_used = 1
number_easy = random.randint(1, 10)
number_medium = random.randint(1, 20) 
number_hard = random.randint(1, 50) 



while game_category == easy and chances < 6:
    guess = int(input('Guess a number between 1-10: '))
    if guess == number_easy:
        print('You got it right')
        break
    else:
        if chances_used < 6:
            print('Try again, you have used {} out of 6 chances you have'.format(chances_used))
        else:
            print('Game Over!')
   
    chances +=1
    chances_used +=1
while game_category == medium and chances < 4:
    guess = int(input('Guess a number between 1-20: '))
    if guess == number_medium:
        print('You got it right')
        break
    else:
        if chances_used < 4:
            print('Try again, you have used {} out of 4 chances you have'.format(chances_used))
        else:
            print('Game Over!')
        
    chances +=1
    chances_used +=1
    
while game_category == hard and chances < 3:
    guess = int(input('Guess a number between 1-50: '))
    if guess == number_hard:
        print('You got it right')
        break
    else:
        if chances_used < 3:
            print('Try again, you have used {} out of 3 chances you have'.format(chances_used))
        else:
            print('Game Over!')
        
    chances +=1
    chances_used +=1
    

    # Thank You!