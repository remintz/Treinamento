numero = int(input('Qual é o número? '))
dividendo = numero
divisor = 1
divisores = []
while (divisor <= dividendo):
  if (dividendo % divisor == 0):
    divisores.append(divisor)
  divisor = divisor + 1
print('Os divisores do número %d são: %s' % (dividendo, divisores))

