from messages import display_messages
import random

print('Starting project again')


while True:
    resposta = input('Deseja um conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()
        