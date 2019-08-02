import math
#esse comando é usado para importar módulos

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = ((b ** 2) - (4 * a * c))

if delta < 0:
  print("Essa equação não possui raizes reais!!!")
elif delta == 0:
  x = (-b / (2 * a))
  print("O valor dessa equação é igual ao delta: ", delta)
  print("O valor de x1 e x2 é: ", x)
elif delta > 0:
  xUm = (- b + (math.sqrt(delta))) / (2 * a)
  xDois = (- b - (math.sqrt(delta))) / (2 * a)
  print("O valor de delta é:", delta)
  print("O valor de x1 é: ", xUm)
  print("O valor de x2 é:", xDois)