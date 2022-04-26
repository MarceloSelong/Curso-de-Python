from math import sin, cos, tan, radians
ang = float(input('Informe o ângulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O \033[31mSeno\033[m é {:.2}'.format(seno))
print('O \033[32mCosseno\033[m é {:.2}'.format(cos))
print('A \033[33mTangente\033[m é {:.2}'.format(tan))
