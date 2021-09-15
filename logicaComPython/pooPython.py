lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(type(lista))
print(lista)

x = 42
print(type(x))

y = 4.34
print(type(y))


tupla = (1,45)
print(type(tupla))

x = [3, 6, 9]
y = [45, "abc"]
print(x[1])


x = [3, 6, 9]
x[2] = 99
x.append(50)
print(x)

y = [45, 'abc', 8]
last = y.pop()
print(last)


# criando classe
class animal:             #cabeçalho
    pass                  #Corpo

"""if__name__== '__main__': ##quando dessejamos saber se o que estamso executando
    x = animal()        #animal 1
    y = animal()        #animal 2
    y2 = y              #Alias
    print(y == y2)
    print(y == x)
"""

#classe animal
class animal:
    pass
x = animal()
y = animal()

x.name = 'Gata'
x.born_year = '2019'
x.pelo = 'branco'
x.patas ='4'

y.name = 'Cachorro'
y.born_year = '2019'
y.pelo = 'preto'
y.patas = '5'

print(x.name)
print(y.name)
print(x.born_year)
print(x.pelo)

x.__dict__
y.__dict__

list.__dict__
tuple.__dict__

def oi (obj):
    print('Miau. Eu sou o gato '+ obj.name + '!')

class animal:
    pass

x = animal()
x.name = 'Bilbo'
x.pelo = 'branco'
oi(x)

def miau(obj):
    print('Miau!')

