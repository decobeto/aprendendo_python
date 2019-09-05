numero = int(input("Digite um número:"))

resto_tres = numero % 3
resto_cinco = numero % 5

if resto_cinco == 0 and resto_tres == 0:
  print("FizzBuzz")
else:
  print(numero)