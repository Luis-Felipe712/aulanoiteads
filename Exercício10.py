ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = 2023
idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")