idade = int(input('Digite sua idade: '))

if idade >= 16 and idade < 18:
    print('Você pode votar se quiser!')
elif idade >=18:
    print('Você deve votar!')
else:
    print('Você não tem idade suficiente para votar!')