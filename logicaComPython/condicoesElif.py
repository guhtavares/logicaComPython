idade = int(input(' Digite a sua idade: '))
print(idade)
print(type(idade))


if idade >= 18:
    print('Voce ja pode dirigir')

elif idade <= 18:
    print('Voce ainda nao pode dirigir')

#Treinando if e elif

exercicio = int(input('Quantos minutos voce se exercita por dia: '))

if exercicio < 30:
    print(' Voce deveria se exercitar mais: ')
elif exercicio >= 30 and exercicio <= 60:
    print('Voce esta no caminho certo')
elif exercicio > 60 and exercicio <= 120:
    print('Voce e um atleta')
else:
    print('Uau! voce se exercita muito')