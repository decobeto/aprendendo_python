print("Digite uma sequência de valores terminada em 0!")
soma = 0
valor = 1

while valor != 0:
  valor = int(input("Digite um valor a ser somado: "))
  soma = soma + valor

print("A soma total dos valores é: ", soma)