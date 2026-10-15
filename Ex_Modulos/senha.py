"""Neste exercício, você deve programar um módulo composto por 4 funções
que, juntas, servirão para determinar se uma senha é boa ou não. Uma boa
senha deve ter:
a. Pelo menos 8 caracteres (1a função)
b. Pelo menos uma letra maiúscula (2a função)
c. Pelo menos uma letra minúscula (3a função)
d. Pelo menos um número (4a função)

Cada função deve retornar true ou false para a senha recebida.
Faça também um programa principal que leia uma senha do usuário, chame
cada função de verificação e relate se a senha é boa ou não.
"""
def num_caracteres(senha):
    nsenha=senha
    if len(nsenha) != 8:
        return False
    else:
        return True

def teste_maiuscula(senha):
    teste=False
    teste_senha=senha
    for char in senha:
        if char.isupper():
            teste= True
            break
    return teste

def teste_minuscula(senha):
    teste=False
    teste_senha=senha
    for char in senha:
        if char.islower():
            teste= True
            break
    return teste

def teste_num(senha):
    tsenha=senha
    tem_num= any(char.isdigit() for char in tsenha)
    return tem_num

def gerasenha():
    senha_usuario=str(input("Digite uma senha que tenha 8 digitos, 1 maiúscula, 1 minúscula e um número: "))
    teste=False
    while teste==False:
        if num_caracteres(senha_usuario) == False or teste_maiuscula(senha_usuario) == False or teste_maiuscula(senha_usuario) == False or teste_num(senha_usuario) == False:
            senha_usuario=str(input("ERRO! A senha deve ter 8 digitos, 1 maiúscula, 1 minúscula e um número.\nTente novamente: "))
        else:
            teste=True
    print("Senha correta! Salvo.")



    