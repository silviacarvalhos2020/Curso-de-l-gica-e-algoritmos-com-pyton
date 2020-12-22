#Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
#π= 3,14 
#r= raio
#float(input('Digite a área:')) 
#area= π . r2
#print (f'{area:.2f} equivalem área do círculo')

#correto
pi = 3.1415926
raio = float(input('Digite o raio do círculo: '))
area = pi * (raio ** 2)
print(f'A área de um círculo de raio {raio} é {area:.2f}m².')