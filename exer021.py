#Algoritmo para executar Mp3
import mp3play

filename = r'C:\Users\Marcelo\Desktop\Estudos\Pycharm Projects\musica.mp3'
clip = mp3play.load(filename)

clip.play(clip)
