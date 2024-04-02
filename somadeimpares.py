numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Ana', 'Bia', 'Carlos', 'Daniel']
ano = [1995, 2024]

soma_impares = 0

for numero in numeros:
    if numero % 2 !=0:
        soma_impares += numero
        
print(soma_impares)