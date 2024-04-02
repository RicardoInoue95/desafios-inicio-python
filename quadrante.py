def coordenadas_quadrante():
    print('Digite a coordenada x: ')
    x = int(input())
    print('Digite a coordenada y: ')
    y = int(input())
    
    if x > 0 and y > 0:
        print('Primeiro quadrante')
    elif x < 0 and y > 0:
        print('Segundo quadrante')
    elif x < 0 and y < 0:
        print('Terceiro quadrante')
    elif x > 0 and y < 0:
        print('Quarto quadrante')
    else:
        print('Origem')
    
coordenadas_quadrante()
