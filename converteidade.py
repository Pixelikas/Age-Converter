
# Cria variáveis e armazena os dados digitados pelo usuário
anoNascimento = int(input('Digite o ano do seu nascimento: '))
anoAtual = int(input('Digite o ano atual: '))

# Realiza os cálculos de conversão
idadeAnos = anoAtual - anoNascimento
idadeMeses = idadeAnos * 12
idadeSemanas = idadeAnos * 52
idadeDias = idadeAnos * 365

# Mostra na tela a idade convertida em ano, meses, semanas e dias
print(f'\n>>>> Sua idade convertida <<<<\n\nAnos: {idadeAnos}\nMeses: {idadeMeses}\nSemanas: {idadeSemanas}\nDias: {idadeDias}\n')


