trabalho = input('Voce deve trabalhar hoje ?')
dia = input('o dia esta bonito ?')
preguica = input(' Voce esta com preguica ?')

# loop da vida

if trabalho == 'sim':
    print('E uma pena')
elif trabalho == 'nao':
    print('Aproveite o dia')

if dia == 'sim' and trabalho == 'nao':
    print('Aproveite para caminhar')
elif dia == 'nao' and trabalho == 'nao':
    print('Aproveite e assista um filme')

if preguica == 'sim' and trabalho == 'nao':
    print('Aproveita e dorme mais')
elif preguica == 'nao' and trabalho == 'sim':
    print('Que tal estudar Python ?')
