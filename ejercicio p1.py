numeros = []
print("Por favor, ingresa 10 números enteros:")

while len(numeros) < 10:
  try:
    num = int(input(f"Número {len(numeros) + 1}: "))
    numeros.append(num)
  except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")

opcion = 0

while opcion != "4":
  print("\n¿Cómo quieres ver la lista?")
  print("--- MENÚ ---")
  print("1. De menor a mayor")
  print("2. De mayor a menor")
  print("3. Mostrar el número del medio")
  print("4. Salir")

  opcion = input("Elige una opción (1, 2, 3 o 4): ")

  print("\n--- RESULTADO ---")
  match opcion:
    case "1":
      print("Lista de menor a mayor:", sorted(numeros))