#Criando String e concatenando  
rua ='Rua do catete'
numero = "153"
bairro = 'Catete'
cidade = 'rio de janeiro'
estado = "Rj"
cep = '22220-000'

endereco = rua + numero + bairro + cidade + estado + cep
print (endereco)

rua ='Rua do catete, '
numero = "153, "
bairro = 'Catete, '
cidade = 'rio de janeiro, '
estado = "Rj, "
cep = '22220-000'

print (endereco)
endereco = rua + numero + bairro + cidade + estado + cep

#letraMaiusculas
endereco_maiuscula = endereco.upper()
print(endereco_maiuscula)


#letraMinuscula
endereco_maiuscula = endereco.lower()
print(endereco_maiuscula)