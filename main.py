
from messages import display_messages
import random
import time


print('starting project 3..2..1..')
time.sleep(3)

while True:
    resposta = input('Deseja um conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()
        