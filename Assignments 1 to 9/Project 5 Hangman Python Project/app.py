import random 
words = ['enum' , 'python' , 'colab' , 'vscode' , 'game']

word = random.choice(words)
guessed_letters = []
attempts = 6

print('Welcome to hangman game project 8')
print('_' * len(word))

while attempts > 0 :
    guess = input('\n guess the letter :').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('Write one alphabate only!')
        continue
    if guess in guessed_letters:
        print('this letter is already guess choose another letter')
        continue
    guessed_letters.append(guess)

    if guess in word:
        print('correct guess!')
    else:
        attempts -= 1
        print(f'wrong {attempts} attempts')

    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word]) 
    print(display_word)       

    if '_' not in display_word:
        print(f'Congration! the correct word is {word}')
        break
    else:
        print(f'game over ! the correct word is {word}')    