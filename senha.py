def senha_usuario():
    print('Digite seu login: ')
    usuario = input()
    print('Digite sua senha: ')
    senha = input()
    if usuario == 'bolt' and senha == '1234':
        print('Acesso permitido')
    else: 
        print('Acesso negado')
        
senha_usuario()