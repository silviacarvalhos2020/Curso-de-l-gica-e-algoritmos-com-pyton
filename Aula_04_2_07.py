#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
#Área = 6 m² . 6 m² = 36 m²
lado = float(input('Digite o lado do quadrado:'))
area = lado ** 2 
dobro = area * 2 
print (f' O dobro da área de um quadrado de lado é {lado:.2f} m é {dobro:.2f}')