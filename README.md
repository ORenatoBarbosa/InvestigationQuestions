# InvestigationQuestions

Perguntas e Repostas para achar o suposto assasino de um crime

print
'Programa Detetive'
print
'Responda as perguntas abaixo com S (sim) ou N (nao)'

perguntas = ('Qual seu nome completo?',
             'Voce telefonou para a vitima nos ultimos 15 dias? ',
             'Voce esteve no local do crime? ',
             'Voce mora perto da vitima? ',
             'Voce devia para a vitima? ',
             'A vitima devia para voce?',
             'Voce trabalhou para a vitima?',
             'voce se relacionou sexualmente com a vitima?',
             'voce se encontrou com a vitima nos ultimos 15 dias?',
             'voce mora perto do local do crime?',
             'Voce sentia algum sentimento de ódio, raiva,repugnância ou vingança pela vítima?',
             'voce possui antecedentes criminais?')

respostas = []

for pergunta in perguntas:
    respostas.append (input(pergunta).upper())

classificacao = 0
for resposta in respostas:
    if (resposta == 'S'):
        classificacao += 1
