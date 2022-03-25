# InvestigationQuestions

print
'Programa Detetive'
print
'Responda as perguntas abaixo com S (sim) ou N (nao)'

perguntas = ('Voce telefonou para a vitima? ',
             'Voce esteve no local do crime? ',
             'Voce mora perto da vitima? ',
             'Voce devia para a vitima? ',
             'A vitima devia para voce?',
             'Voce trabalhou para a vitima?',
             'voce se relacionou sexualmente com a vitima?',
             'voce se encontrou com a vitima nos ultimos 7 dias?',
             'voce mora perto do local do crime?',
             'voce possui antecedentes criminais?')

respostas = []

for pergunta in perguntas:
    respostas.append (input(pergunta).upper())

classificacao = 0
for resposta in respostas:
    if (resposta == 'S'):
        classificacao += 1

if (classificacao < 2):
    print('Inocente')
elif (classificacao == 2):
    print('nao tão Suspeito')
elif (classificacao == 4):
    print('um tanto Suspeito')
elif (classificacao == 6):
    print('muito suspeito')
elif (classificacao == 7):
    print('sob investigação')
elif (classificacao <= 8):
    print('Cumplice')
else:
    print('Assassino')
# RENATO BARBOSA investigação
