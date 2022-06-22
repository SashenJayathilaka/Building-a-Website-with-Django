started = False

while True:

    option = '''
start - to start the car
stop - to stop the car
quit - to exit
    '''

    guess_count = 0
    count_limit = 3

    enter_the_game = input(">")

    if enter_the_game.upper() == 'START':
        if started:
            print('Car is Already Started')
        else:
            started = True
            print('Car started.... Ready to go!')

    elif enter_the_game.upper() == 'STOP':
        if not started:
            print('Car is Already stop')
        else:
            started = False
            print('Car stopped.')

    elif enter_the_game.upper() == 'HELP':
        print(option)
    elif enter_the_game.upper() == 'QUIT':
        break
    else:
        print("I don't understand that.... Type 'help' command")