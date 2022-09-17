# Validação de Nota (bee_1117)

x, y = (-1.0,-1.0)

while (x < 0.0 or x > 10.0) or (y < 0.0 or y > 10.0):
    if x < 0.0 or x > 10.0:
        x = float(input())
        if x < 0.0 or x > 10.0:
            print('nota invalida')
    if y < 0.0 or y > 10.0:
        y = float(input())
        if y < 0.0 or y > 10.0:
            print('nota invalida')

print(f'media = {(x+y)/2:.2f}')
