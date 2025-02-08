#Escreva um programa que peça ao usuário uma senha e verifique se ela está correta
# (a senha correta é "python123").

#leitura de dados
senha = input('Digite a senha:')

#processamento
if senha == 'python123':
    print('\nSenha correta!')
else:
    print('\nSenha incorreta!')