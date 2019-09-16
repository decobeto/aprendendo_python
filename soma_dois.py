quantidade = int(input("Digite o número de vezes em que a soma vai ser repetida: "))
soma = 0
valor = 1
i = 0

while i < quantidade:
  valor = int(input("Digite um valor a ser somado: "))
  soma = soma + valor
  i = i + 1

print("A soma total dos valores é: ", soma)