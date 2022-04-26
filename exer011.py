print('Cálculo de tinta necessária')
l = float(input('Informe a \033[34mlargura\033[m da parede em \033[31mmetros\033[m: '))
a = float(input('Informe a \033[34maltura\033[m: '))
print('A quantidade de tinta necessária para pintar esta parede de \033[34m{}m²\033[m são \033[31m{}\033[m '
      'litros de tinta. Sabendo que \033[34m2L\033[m pintam \033[31m2m²\033[m.'.format(l*a, (l*a)/2))
