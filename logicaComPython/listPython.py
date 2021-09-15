frutas = ['banana', 'laranja', 'abacate', 'melancia', 'caju', 'abacaxi']
saldo_alunos = [500.00, 1200.00, 1000.00, 600.00, 50000.00]
num_pacientes = [25, 36, 50, 45, 22, 33, 89]

print(frutas)
print(saldo_alunos)
print(num_pacientes)

#permitte duplicata
frutas_dup = ['banana', 'laranja', 'abacate', 'melancia', 'caju', 'abacaxi', 'banana', 'laranja', 'abacate',]
print(frutas_dup)


print(len(saldo_alunos))
print(len(num_pacientes))

variados = [10, 2.5, 'Python']
print(variados)

print(frutas[2])
print(frutas[3])

frutas.append('morango')
print(frutas)


saldo_alunos.extend(num_pacientes)
print(saldo_alunos)

