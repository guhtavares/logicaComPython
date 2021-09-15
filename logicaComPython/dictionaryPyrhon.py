cod_uf = {
    21 : 'Maranhao',
    22 : "Piaui",
    23 : 'Ceara',
    24 : 'Rio Grande do Norte',
    25 : ' Paraiba',
    26 : 'Pernambuco',
    27 : 'Alagoas',
    28 : 'Sergipe',
    29: 'Bahia'
}

print(type(cod_uf))
print(cod_uf)

#valores ordenados
print(cod_uf.values())


#acessando os valores
print(cod_uf.get(29))
print(cod_uf.get(22))

print(cod_uf.keys())

#adicionando valores
cod_uf[30] = 'Estado Vira-Lato Caramelo'
print(cod_uf)