temp = float(input('Digite a temperatura: '))

if temp < 15:
    print('Está frio!')
elif temp >= 15 and temp <= 30:
    print('Está agradável!')
else:
    print('Está quente!')