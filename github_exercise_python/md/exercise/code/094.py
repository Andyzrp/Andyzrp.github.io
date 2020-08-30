import random
import time

play_it = input("do you want to play it.('y' or 'n')")
i = random.randint(0, 10 ** 32)
while play_it == 'y':
    start = time.process_time()
    a = time.time()
    guess = int(input('please input number you guess:'))
    while guess != i:
        if guess > i:
            print('please input a little smaller')
            guess = int(input('input your guess:'))
        else:
            print('please input a little bigger')
            guess = int(input('input your guess:'))
    end = time.process_time()
    b = time.time()
    var = (end - start) / 18.2
    print(var)
    if var < 15:
        print('you are very clever!')
    elif var < 25:
        print('you are normal!')
    else:
        print('you are stupid!')
    print('Congradulations')
    print(f'The number you guess is {i}')
    play_it = input("do you want to play it.('y' or 'n')")
