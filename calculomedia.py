numeros = [1,2,3,4,5,6,7,8,9,10]

try:
    media = sum(numeros)/len(numeros)
    print(f'A média dos números é: {media}')
    
except ZeroDivisionError:
    print('Erro: A lista está vazia')
    
except Exception as e: 
    print(f'Erro: {e}')