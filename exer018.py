from math import sin, cos, tan, radians
ang = float(input('Informe o ângulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O Seno é {:.2}'.format(seno))
print('O Cosseno é {:.2}'.format(cos))
print('A Tangente é {:.2}'.format(tan))
