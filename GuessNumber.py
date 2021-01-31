# Este é um jogo de adivinhar o número.

import random

secretnumber = random.randint(1, 20)

print("I am thinking of a number betwween 1 and 20.")

for guessTaken in range(1, 7):
    print("Take guess")
    guess = int(input())

    if guess < secretnumber:
        print("Your guess is too low.") # Seu palpite é muito Alto
    elif guess > secretnumber:
        print('Your guess is too high.') # Seu palpite é muito Baixo
    else:
        break

if guess == secretnumber:
     print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!') # Bom trabalho você advinhou meu número em
else:
    print('Nope. The number I was thinking of was ' + str(secretnumber)) # Não. O número que eu estava pensando era
