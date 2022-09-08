while True:
    user_input = input('>').lower()
    choices = ['rock', 'paper', 'scissors']

    import random

    comp_choice = random.choice(choices)

    if user_input == 'rock' and comp_choice == 'rock':
        print(comp_choice)
        print('tie')
    if user_input == 'rock' and comp_choice == 'paper':
        print(comp_choice)
        print('i win')
    if user_input == 'rock' and comp_choice == 'scissors':
        print(comp_choice)
        print('you win')
    if user_input == 'paper' and comp_choice == 'rock':
        print(comp_choice)
        print('you win')
    if user_input == 'paper' and comp_choice == 'paper':
        print(comp_choice)
        print('tie')
    if user_input == 'paper' and comp_choice == 'scissors':
        print(comp_choice)
        print('i win')
    if user_input == 'scissors' and comp_choice == 'rock':
        print(comp_choice)
        print('i win')
    if user_input == 'scissors' and comp_choice == 'paper':
        print(comp_choice)
        print('you win')
    if user_input == 'scissors' and comp_choice == 'scissors':
        print(comp_choice)
        print('tie')
    if user_input == 'quit':
        print('quitting')
        break

print('that was fun')
