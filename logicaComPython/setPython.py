cidade = {'Belo Horizonte', 'Manaus', 'Fortaleza', 'Natal'}
print(type(cidade))
print(cidade)

#não permite valores duplicados
cidade_repet = {'Belo Horizonte', 'Manaus', 'Fortaleza', 'Natal', 'Belo Horizonte', 'Manaus', 'Fortaleza', 'Natal'}
print(cidade_repet)

#checando valores
cidade = {'Belo Horizonte', 'Manaus', 'Fortaleza', 'Natal'}
print('Manaus' in cidade)
print('Recife' in  cidade)

#adicionando item 
cidade.add('Porto Alegre')
print(cidade)

#unindo sets
cidade_2 = {'Recife', 'Salvador', 'Campo Grande'}
cidade.update (cidade_2)
print(cidade)