import random

choices = ['rock' , 'paper' , 'scissors']

player_choice = input('Enter rock , paper scissor :').lower

computer_choice = random.choices(choices)

if player_choice == computer_choice:
    print(f'both choice {player_choice} .Its a tie')
elif player_choice == 'rock' and computer_choice == 'scissor':
    print(f'player wins! {player_choice} beat {computer_choice}')
elif player_choice == 'paper' and computer_choice == 'rock':
    print(f'player wins! {player_choice } beats {computer_choice}') 
elif player_choice == 'paper' and computer_choice == 'paper':
    print(f'player wins! {player_choice } beats {computer_choice}')  

else:
    print(f'computer wins! {computer_choice} BEATS {player_choice}')          
