import random
UserWon = 'User gana!'
IgridWon = 'Computer gana!'
Options_Tuple = ('piedra', 'papel', 'tijera')
computer_Wins = 0
User_wins = 0
rounds = 1
while True:
    
    print ('*'*10)
    print('Round ', rounds)
    print ('*'*10)
    
    User = input('ingresa piedra, papel o tijeras: ')
    Use = User.lower()
    
    rounds += 1
    
    Igrid_Laptop = random.choice(Options_Tuple)

    print('User option: ', User)
    print('Computer option: ', Igrid_Laptop)

    if not Use in Options_Tuple:
        print('Esa es una opcion invalida')


    if User == Igrid_Laptop:
        print("Es un empate")
    elif User == 'papel':
        if Igrid_Laptop == 'piedra':
            print('papel gana a piedra')
            print(UserWon)
            User_wins += 1
        else:
            print('tijera gana a papel')
            print(Igrid_Laptop)
            computer_Wins = 0
    elif User == 'tijera':
        if Igrid_Laptop == 'papel':
            print('tijera gana a papel')
            print(UserWon)
            User_wins += 1
        else:
            print('piedra gana a tijera')
            print(Igrid_Laptop)
            computer_Wins = 0
    elif User == 'piedra':
        if Igrid_Laptop == 'tijera':
            print('piedra gana tijera')
            print(UserWon)
            User_wins += 1
        else:
            print("papel gana a piedra")
            print(Igrid_Laptop)
            computer_Wins = 0
    if computer_Wins == 2:
        print('El ganador es la computadora')
    if User_wins == 2:
        print('El ganador es el usuario')
    


