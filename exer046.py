#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#indo de 10 até 0,
#com uma pausa de 1segundo entre eles.
from time import sleep
import emojislib as emojis
emoji = emojis.by_name('fireworks')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.char)
print('Fim')
