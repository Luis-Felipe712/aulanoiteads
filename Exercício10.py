from datetime import date

ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Você pode votar esse ano. Sua idade é: ", idade)
else:
    print("Você não pode votar esse ano. Sua idade é: ", idade)