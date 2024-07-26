from random import randint

def user_interface(options):
    for index, options in enumerate(options):
        print(f'{index} = {options}')
    return int(input('\nDigite sua escolha? '))
    
def computer_choice(content):
    return randint(0, len(content)-1)
    
def check_result(choices, player, computer, rules):
    if player == computer:
        return 'Empate'
    
    if choices[computer] in rules[choices[player]]:
        return 'Você ganhou'

    return 'O Computador ganhou'

def play():
    print('\nBem vindo ao Pedra, Papel, Tesoura, Lagarto, Spock\n')

    optionsList = ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']

    rules = {
        'Pedra': ['Tesoura', 'Lagarto'],
        'Papel': ['Pedra', 'Spock'],
        'Tesoura': ['Papel', 'Lagarto'],
        'Lagarto': ['Spock', 'Papel'],
        'Spock': ['Tesoura', 'Pedra'],
    }

    playerResult = user_interface(optionsList)
    computerResult = computer_choice(optionsList)

    print(f'Escolha do jogador: {optionsList[playerResult]}')
    print(f'Escolha do computador: {optionsList[computerResult]}')

    print(f'\n{check_result(optionsList, playerResult, computerResult, rules)}')

def main():
    playAgain = ''
    while playAgain.lower() != 'n':
        play()
        print(f'\nDeseja jogar novamente? ')
        playAgain = input('Digite \'S\' para sim ou \'N\' para não: ')

main()