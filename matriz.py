#matriz
m1 = [[1,2,3],[4,5,6],[7,8,9]]
#ou                    #ij ij ij
m2 = [[1,2,3],       #1 00 01 02
      [4,5,6],       #2 10 11 12
      [7,8,9]]       #3 20 21 22
ordem = 3

#Faça um programa que calcule em uma matriz 3x3 e escreva o valor das seguintes somas: 
#a)	da linha 2 (linha 2 o índice i é 1);
somaLinha2 = 0
for i in range(ordem):
  for j in range(ordem):
    if i == 1:
      somaLinha2 = somaLinha2 + m1[i][j]
print("soma linha 2:",somaLinha2)

#b)	da coluna 3;
somaColuna3 = 0
for i in range(ordem):
  for j in range(ordem):
    if j == 2:
      somaColuna3 += m1[i][j]
print("soma coluna 3:",somaColuna3)

#c)	da diagonal principal;
somaDP = 0
for i in range(ordem):
  for j in range(ordem):
    if i == j:
      somaDP += m1[i][j]
print("soma Diagonal Princial:",somaDP)

#d)	da diagonal secundária;
somaDS = 0
for i in range(ordem):
  for j in range(ordem):
    if i+j == ordem -1:
      somaDS += m1[i][j]
print("soma Diagonal Secundaria:",somaDS)

#e)	acima da diagonal secundária;
somaAcimaDS = 0
for i in range(ordem):
  for j in range(ordem):
    if i+j < ordem -1:
      somaAcimaDS += m1[i][j]
print("soma Acima Diagonal Secundaria:",somaAcimaDS)

#f)	abaixo da diagonal secundária;
somaAbaixoDS = 0
for i in range(ordem):
  for j in range(ordem):
    if i+j >= ordem:
      somaAbaixoDS += m1[i][j]
print("soma Abaixo Diagonal Secundaria:",somaAbaixoDS)

#g)	acima da diagonal principal;
somaAcimaDP = 0
for i in range(ordem):
  for j in range(ordem):
    if i < j:
      somaAcimaDP += m1[i][j]
print("soma Acima Diagonal Principal:",somaAcimaDP)

#h)	abaixo da diagonal principal;
somaAbaixoDP = 0
for i in range(ordem):
  for j in range(ordem):
    if i > j:
      somaAbaixoDP += m1[i][j]
print("soma Abaixo Diagonal Principal:",somaAbaixoDP)

#i)	de todos os elementos da matriz. 
somaTodos = 0
for i in range(ordem):
  for j in range(ordem):
    somaTodos += m1[i][j]
print("soma todos os elementos:",somaTodos)

