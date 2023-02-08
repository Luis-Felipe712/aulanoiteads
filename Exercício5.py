print ("Cadastro de Clientes\n0 - Fim\n1 - Inclui\n2 - Altera\n3 - Exclui\n4 - Consulta")

valor = int(input("Insira um número para realizar uma ação: "))

if valor == 0:
    print("Fim")
elif valor == 1:
    print("Inclui")
elif valor == 2:
    print("Altera")
elif valor == 3:
    print("Exclui")
elif valor == 4:
    print("Consulta")
else:
    print("Item não encontrado")