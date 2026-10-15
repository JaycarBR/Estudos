"""
Crie um módulo com 3 funções que, juntas, servirão para a criação
de placas de veículos no novo padrão do Mercosul. O novo padrão é
composto por quatro letras e três números: AAA0A00
Assim, sua primeira função deve gerar 4 letras aleatoriamente, a
segunda função deve gerar 3 números inteiros aleatoriamente e a
terceira função deve juntar as letras e os números no padrão correto:
letra-letra-letra-num-letra-num-num (AAA0A00).

Escreva um programa principal que chama as três funções e exibe a
placa criada.    
"""

def geraletras():
    import random
    import string
    listal=[]
    for x in range(4):
        letra = random.choice(string.ascii_letters)
        listal.append(letra.upper())
    print(listal)
    return listal

def geranum():
    from random import randrange
    listan=[]
    for x in range(3):
        listan.append(randrange(0, 10))
    print(listan)
    return listan

def geraplaca():
    placa=geraletras()
    numeros=geranum()
    placa.insert(3,str(numeros[0]))
    for x in range(1, 3):
        placa.append(str(numeros[x]))
    placa="".join(placa)
    placa=placa.replace("-","")
    print(placa)
    
