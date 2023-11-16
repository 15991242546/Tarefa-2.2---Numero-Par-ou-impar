# Escreva um programa que solicite ao usuário um número e verifique se esse número é par ou ímpar

print ('O número escolhido é impar ou par?')
numero = int (input ('Digite um numero '))
resultado = numero % 2
if resultado == 0:
    print ('O numero {} é PAR'. format (numero))
else: 
    print ('O numero {} é IMPAR'. format (numero))
print('.'*30)




