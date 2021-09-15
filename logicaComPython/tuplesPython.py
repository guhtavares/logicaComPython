frutas = ('banana', 'laranja', 'abacate', 'melancia', 'caju', 'abacaxi')
saldo_alunos = (500.00, 1200.00, 1000.00, 600.00, 50000.00)
num_pacientes = (25, 36, 50, 45, 22, 33, 89)

print(frutas[1])
print(frutas[1:4])
print(frutas[0:6])

#permite duplicados
saldo_alunos_dup = (500.00, 1200.00, 1000.00, 600.00, 50000.00, 500.00, 1200.00, 1000.00, 600.00, 50000.00)
print(saldo_alunos_dup)

#juntar tuplas 
tupla_junto = frutas + num_pacientes
print(tupla_junto)

print(type(tupla_junto))

#contar valores repetidos 
num_pacientes_x = (25, 36, 50, 45, 22, 33, 89, 25, 36, 50, 45, 22, 33, 89, 25, 36, 50, 45, 22, 33, 89)


print(num_pacientes_x.count(45))