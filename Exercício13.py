lados = int(input("Informe o número de lados do polígono: "))

if lados == 3:
    print("TRIÂNGULO")
    # Cálculo da área de um triângulo
elif lados == 4:
    print("QUADRADO")
    # Cálculo da área de um quadrado
elif lados == 5:
    print("PENTÁGONO")
else:
    print("Polígono não identificado.")