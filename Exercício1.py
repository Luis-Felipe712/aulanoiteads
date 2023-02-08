N1 = float(input("Insira a nota 1: "))
N2 = float(input("Insira a nota 2: "))
N3 = float(input("Insira a nota 3: "))
ME = float(input("Insira o valor da média dos exercícios: "))

MA = (N1 + N2*2 + N3*3 + ME)/7

if MA >= 9:
    print("Sua média final foi: ", MA, ". Parabéns, essa é uma média alta!")
elif MA < 4:
    print("Sua média final foi: ", MA, ". Atenção, essa é uma média baixa!")
else:
    print("Sua média final foi: ", MA)