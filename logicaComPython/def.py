def soma (x, y):
    print(x + y)

soma(10, 20)
print(soma)

soma(50, 50)
print(soma)


def imc(peso, altura):
    imc = peso /(altura **2)
    if imc < 18.5:
        print('Magro')
    elif imc >= 18.5 and imc <= 24.9:
        print('Normal')
    elif imc >= 25.0 and imc <= 29.9:
        print('sobrepeso')
    elif imc >= 30.0 and imc <= 39.9:
        print("Obesidade I")
    else:
        print('Obesidade II')
    return

imc(115, 1.83)