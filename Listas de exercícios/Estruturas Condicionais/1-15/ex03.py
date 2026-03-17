num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num2 > num1:
    print(f'O número {num2} é maior do que o {num1}')
elif num1 > num2:
    print(f'O número {num1} é maior do que o {num2}')
else: 
    print('Os dois números são iguais')