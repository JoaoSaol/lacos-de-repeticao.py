a = int(input('Primeiro Bimestre: '))
while a > 10:
	a = int(input('Você digitou errado, permitimos valores de 0 a 10. Digite novamente sua nota do Primeiro Bimestre: '))
	
b = int(input('Segundo Bimestre: '))
while b > 10:
	b = int(input('Você digitou errado, permitimos valores de 0 a 10. Digite novamente sua nota do Segundo Bimestre: '))
	
c = int(input('Terceiro Bimestre: '))
while c > 10:
	c = int(input('Você digitou errado, permitimos valores de 0 a 10. Digite novamente sua nota do Terceiro Bimestre: '))
	
d = int(input('Quarto Bimestre: '))
while d > 10:
	d = int(input('Você digitou errado, permitimos valores de 0 a 10. Digite novamente sua nota do Quarto Bimestre: '))
	
media = (a + b + c + d) / 4
print('Sua media anual é: {}'.format(media))
