def idade():
    print('Digite sua idade: ')
    idade = int(input())
    if idade <= 12:
        print('Criança')
    elif idade >= 13 and idade <= 18:
        print('Adolescente')
    else:
        print('Adulto')
        
idade()