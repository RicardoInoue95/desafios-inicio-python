numeros = [1,22,37,42,59,61]
soma=0


try:
    for numero in numeros:
            soma += numero
    print(f"A soma de todos é: {soma}")
        
except Exception as e:
    print('Erro: A lista contém valores não numéricos')