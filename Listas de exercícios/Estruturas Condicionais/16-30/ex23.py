num = int(input('Digite um número: '))

if num % 2 == 0:
    print('O seu número é múltiplo de 2')
elif num % 3 == 0:
    print('O seu número é múltiplo de 3')
elif num % 2 == 0 and num % 3 == 0:
    print('O seu número é múltiplo de 2 e 3')
else:
    print('O seu número não é multiplo nem de 2 nem de 3')