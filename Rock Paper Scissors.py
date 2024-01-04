import random

def play():
    user = input("What's your choice ?\n 'r' for Rock,'p' for Paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a Tie'

    if is_win(user, computer):
        return 'You won'

    return 'You lost'

def is_win(player, opponent):
    # return true if player wins
    # r > s , s > p , p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

choice = 1
while choice != '2':
    choice = input("Press '1' to start the game\nPress '2' to end game.\n")

    if choice == '1':
        result = play()
        print(result)

    elif choice == '2':
        exit()
