#  Escreva um programa que peça um número inteiro positivo ao usuário e faça uma contagem regressiva até 0, imprimindo cada número.

x = float(input())
while x>0:
  print(x)
  x=x-1
print("fim")






# Peça números ao usuário e some-os. Pare quando o usuário digitar um número negativo e exiba a soma total.

soma = 0
while True:
    num = float(input())
    if num < 0:
        break
    soma = soma + num
print(soma)

