numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Ana', 'Bia', 'Carlos', 'Daniel']
ano = [1995, 2024]


numero=int(input('Digite o número para ver a tabuada:'))

print(f'Tabuada do {numero}')
for i in range(10):
    print(f'{numero} x {i+1} = {numero*(i+1)}')
