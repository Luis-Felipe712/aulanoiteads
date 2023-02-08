a1 = int(input("Informe o valor inicial: "))
n = int(input("Informe a quantidade de termos: "))
q = int(input("Informe a razão (q >= 2): "))

while q < 2:
    print("A razão deve ser maior ou igual a 2.")
    q = int(input("Informe a razão (q >= 2): "))

soma = a1 * (q**n - 1) / (q - 1)

print("A soma dos termos é:", soma)