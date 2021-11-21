import random
import word_list
import asciiDiagrams


print(asciiDiagrams.logo)

dictionary = dict([(chr(i), 'no') for i in range(97, 123)])

words = word_list.wordlist
chosen_word = random.choice(words)
lives = 7
print('You have', lives, 'lives')

# Testing code
print(f'Pssst, the solution is {chosen_word}.')


display = []
for letter in chosen_word:
    display.append('_')

while lives > 0:
  if '_' in display:
    guess = input("Guess a letter: ").lower()
    if dictionary[guess] == 'no':
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        if guess not in chosen_word:
            lives -= 1
            print(asciiDiagrams.stages[lives])
            print('You have guessed a wrong letter', ',You have', lives, 'left')
        print(display)
        dictionary[guess] = 'yes'
        if '_' not in display:
            answer = ''.join(display)
            print('The word is', answer, "\nYOU WIN")
    else:
        print("letter has been guessed")

if lives == 0:
    print("YOU LOSE")