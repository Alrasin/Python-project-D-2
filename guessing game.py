wining_num = 7
guess_num = 0
guess_limit = 3

while guess_num < wining_num:
    guess = int(input('Guess: '))
    guess_num += 1
    if guess == wining_num:
        print('You Win')
        break
else:
    print('You Lose')