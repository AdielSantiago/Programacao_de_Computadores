num = int(input('Digite um número: '))

if num > 0:
    print('O seu número é positivo mas não é maior do que 100!')
elif num > 0 and num > 100:
    print('O seu número é positivo e maior do que 100')
elif num == 0:
    print('O seu número é ZERO')
else:
    print('O seu número é negativo!')