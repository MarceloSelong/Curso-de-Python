# Cálculo para encontrar a Hipotenusa
from math import sqrt
catop = float(input('informe o comprimento do Cateto oposto '))
catadj = float(input('Informe o comprimento do Cateto Adjacente '))
hipot1 = (catop**2)+(catadj**2)
hipot2 = sqrt(hipot1)
print('{:.3}'.format(hipot2))
