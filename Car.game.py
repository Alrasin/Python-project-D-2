cmd = ""
while True:
    cmd = input('> ').lower()
    if cmd == "start":
        print('Car started')
    elif cmd == "stop":
        print('Car stopped')
    elif cmd == "help":
        print('''Start - to start the car
Stop - to stop the car
Quit - to exit the program''')
    elif cmd == "quit":
        print('Exit the program')
        break
    else:
        print('Invalid command')




