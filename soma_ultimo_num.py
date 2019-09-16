numero = int(input("Insira números em sequência para soma-lôs: "))
soma = 0

while numero > 0:
  ultimo_valor = numero % 10
  soma = ultimo_valor + soma
  numero = numero // 10
  print("Valor da soma: ", soma)