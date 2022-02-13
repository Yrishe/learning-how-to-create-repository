import random

display_messages = [
    'Seja feliz!',
    'Fique tranquilo, vai acabar tudo bem!'
]

while True:
    resposta = input('Deseja um conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()
        