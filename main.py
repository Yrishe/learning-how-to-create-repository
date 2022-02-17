
from messages import display_messages
import random
import time


print('starting project 3..2..1..')
time.sleep(3)

login_username = [
    'Yarli',
    'Matheus',
    'Bianca'
]

username = input('usuario para login: ')

while True:
    
    while (username not in login_username):
        print()
        print('Usuario Invalido! Tente novamente! ')
        username = input('usuario para login: ')



    resposta = input('Deseja um conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()
    elif (resposta == 'N' or resposta == 'n'):   
        exit() 