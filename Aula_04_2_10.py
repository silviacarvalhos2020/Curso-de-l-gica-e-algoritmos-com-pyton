#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. 
#Parabéns você tirou 9.9 porque tinha colocado mais dois parentes na linha 5, agora está correto, se não tinha tirado 10.

grausCelsius = float(input("Digite a temperatura em Celsius:"))
grausFarenheit = (grausCelsius)* (9.0/5.0) + 32
print(f'{grausCelsius:.2f} graus Celsius correspondem a {grausFarenheit:.2f} graus Farenheit')

