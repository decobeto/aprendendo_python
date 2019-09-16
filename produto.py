print("Digite uma sequência de valores terminada em 0!")
produto = 1
valor = 1

while valor != 0:
  valor = int(input("Digite um valor a ser multiplicado: "))
  produto = produto * valor

print("O produto total dos valores é: ", produto)