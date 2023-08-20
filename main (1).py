import random

class Game:
    def play(self):
        user_choice = input('Rock, Paper, Or Scissors?\n').lower()
        options = ['rock', 'paper', 'scissors']

        if user_choice not in options:
            print('Error: Choose Rock, Paper, or Scissors')
        else:
            comp_choice = random.choice(options)
            print('The Computer chose ' + comp_choice.capitalize())

            if user_choice == comp_choice:
                result = 'TIE'
            elif (user_choice == 'rock' and comp_choice == 'scissors') or \
                 (user_choice == 'scissors' and comp_choice == 'paper') or \
                 (user_choice == 'paper' and comp_choice == 'rock'):
                result = 'YOU WIN'
            else:
                result = 'YOU LOSE'

            print(result)

# Create an instance of the Game class and play the game
game = Game()
game.play()
