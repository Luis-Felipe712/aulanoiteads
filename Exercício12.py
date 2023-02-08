altura = float(input("Informe a altura: "))
sexo = int(input("Informe o sexo (1:feminino 2:masculino): "))

if sexo == 1:
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é:", peso_ideal, "kg.")
elif sexo == 2:
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal é:", peso_ideal, "kg.")
else:
    print("Sexo inválido.")