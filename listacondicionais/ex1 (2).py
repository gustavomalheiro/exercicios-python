numero_1 = input("Entre com o primeiro número: ")
numero_2 = input("Entre com o segundo número: ")

numero_1 = int(numero_1)
numero_2 = int(numero_2)

if numero_1 > numero_2:
    print("Numero 1 é maior que o número 2.")
elif numero_1 == numero_2:
    print("São iguais.")
else:
    print("Numero 2 é maior que o número 1.")
