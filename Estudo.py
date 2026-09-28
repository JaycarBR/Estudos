#não usar acento em nome de variável, diferenciam minúsculas e maiúsculas, não começa nome com nº, aceita "_"
#Variável com todas as letras maiúsculas: Variável CONSTANTE e sem mudança de valor
#variável: espaço na memória aonde se guarda um dado
#3 aspas comenta o texto

"""idade=int(input("Entre com sua idade: ")) #Se não colocar o tipo na entrada, vai entrar como str
nome=input("Entre com seu nome: ") #Se não definir o tipo de entrada, vai entrar como str
print(idade)
print("Minha idade é", idade, "anos")
print("Meu nome é %s e tenho %d anos" % (nome, idade)) # %d = número inteiro, %s = string, %f = número float, %x = número hexadecimal"""

#Para colocar % (porcentagem) em uma string, tem que usar o símbolo "%" 2 vezes

"""pi=3.14
print("O pi vale %.2f" % pi) #O "2" entre . e f indica o número de casas decimais a serem exibidas
print("O pi vale {0:2.3f}" .format(3.14159)) #O "2" entre : e . indica o número mínimo de caracteres a serem exibidos, o "3" entre . e f indica o número de casas decimais a serem exibidas

inteiro=10
real=10.5
complexo=5+3j
texto="exemplo"
tipologico=True

print(type(inteiro))
print(type(real))
print(type(complexo))
print(type(texto))
print(type(tipologico))

valora=8 #valor direto entra como int
valorb=6
soma=valora+valorb
print(valora + valorb)
print(type(soma))"""

""" 
Operadores Aritméticos: 
+  Soma
-  Subtração
*  Multiplicação
@  Multiplicação de matrizes
/  Divisão
// Divisão inteira
%  Resto da divisão
** potenciação: x**y = x elevado a y
"""

"""
PRECISA IMPORTAR a biblioca com "from math import *"

Funções Matemáticas:
abs(x) - valor absoluto de x
sqrt(x) - raiz quadrada de x
pow(x, y) - x elevado a y
log(x) - logaritmo natural de x
log10(x) - logaritmo base 10 de x #(log10(x) = y -> 10**y = x)
sin(x) - seno de x em radianos #sen(x) = cateto oposto/hipotenusa
cos(x) - cosseno de x em radianos #cos(x) = cateto adjacente/hipotenusa
tan(x) - tangente de x em radianos #tan(x) = sen(x)/cos(x) = cateto oposto/cateto adjacente
exp(x) - exponencial de x #exp(x) = e**x, onde e é a base do logaritmo natural, aproximadamente igual a 2.71828
round(x, n) - arredonda x para n digitos
floor(x) - arredonda x para baixo
"""

"""from math import *
print(sqrt(9))"""

"""
Operadores relacionais:
==  Igual a
>  Maior que
<  Menor que
!=  Diferente
>=  Maior ou igual
<=  Menor ou igual
in  Pertence a
is  Identidade de objetos
is not  Negação da identidade de objetos
not in  Negação de pertencer a
"""

"""
valorc=int(input("Entre com o valor c: "))
valord=int(input("Entre com o valor d: "))

if valord > valorc:   #condicional if é equivalente a "se", o código dentro do if só é executado se a condição for verdadeira
    print("O valor d é maior que o valor c")  #a indentação é para indicar que o print faz parte do bloco do if, se não tiver a indentação, o print será executado independentemente da condicional
if valorc > valord:
    print("O valor c é maior que o valor d")
else:   #condicional else é equivalente a "senão", o código dentro do else só é executado se a condição do if for falsa
    print("O valor c é igual ao valor d")

if valord > valorc:
    print("O valor d é maior que o valor c")
elif valord < valorc:   #condicional elif ou if else equivale a "senão se", o código dentro do elif só é executado se a condição do if for falsa e a condição do elif for verdadeira
    print("O valor c é maior que o valor d")
else:
    print("O valor c é igual ao valor d")
    """

"""Operadores lógicos:
and: E condicional, a expressão é verdadeira se ambas as condições forem verdadeiras
or: OU condicional, a expressão é verdadeira se pelo menos uma das condições for verdadeira
xor: OU exclusivo, a expressão é verdadeira se apenas uma das condições for verdadeira
not: NÃO lógico, inverte o valor lógico de uma expressão

OBS: Operadores relacionais sempre retornam valores booleanos (True ou False)
"""

"""
Faça um programa que lê um ano como entrada e verifica se esse ano é bissexto.
Regras para definição de ano bissexto:
Se o ano for divisível por 400 ele é bissexto! Acaba aqui!
Se o ano não for divisível por 400, para ser bissexto ele deve:
Ser divísivel por 4
Não ser divisível por 100
Faça o programa com somente 1 if, 1 else, nenhum elif
"""

"""ano=int(input("Entre com o ano: "))
if ano%400 == 0 or ano%4==0 and ano%100!=0:
    print("O ano %d é bissexto" % ano)
else:
    print("O ano não é bissexto")
"""

"""
ultimo=int(input("Entre com o último número da sequência: "))
i=0
while i <= ultimo:   #condicional while é equivalente a "enquanto", o código dentro do while é executado enquanto a condição for verdadeira
    print(i)
    i += 1   #o += é um operador de atribuição que incrementa o valor da variável"""

"""
while True:   #loop infinito, o código dentro do while é executado para sempre
    print("Loop infinito")""" 

"""
#só funcionam dentro do loop:
break   #comando para sair do loop. Pode ser útil para interromper um loop quando uma condição específica for atendida
continue   #comando para pular para a próxima iteração do loop.
"""

"""while True:
    entrada=int(input("Digite um número para somar ou 0 para sair: "))
    if entrada == "0":
        break
    else:
        somatória=somatória + entrada
print("A somatória é: %d" % somatória)
"""

"""
Comando FOR: Estrutura de repetição que permite iterar sobre uma sequência de elementos

Exemplo: Calcular a somatória dos números de 0 a 99"
somatoria=0
for x in range(0, 100):  #range(i, f, p) - i: início, f: até valores menores que, p: passo (opcional, padrão é 1)
    somatoria= somatoria + x
print(somatoria)
"""

"""
from random import randrange
contagem=0
maior_valor=0
for x in range(0, 100):
    valor = randrange(0, 101)
    if maior_valor < valor:
        contagem += 1
        maior_valor=valor
else:     #A cláusula else só é executada quando a condição do loop se torna falsa. Se usar o break, o else não é executado.
    print("O maior valor é %d, e o valor foi atualizado %d vezes." % (maior_valor, contagem))
"""

#Lista: armazena um conjunto de valores, permite armazenar valores do mesmo tipo ou diferentes(heterogênea), os valores são acessados por um índice
#Lista: ['a', 2, 3.1, 'b'] -> Respectivos índices: [0, 1, 2, 3]
#lista.append(item) adiciona elemento pro final da lista
#lista.insert(índice, item) -> coloca elemento na posição do indice escolhido
#lista.pop(índice) -> retira o elemento do indice escolhido ->se não colocar o indice, ele tira o último elemento
#lista.remove(item) -> vai remover pelo elemento, irá remover apenas o primeiro que encontrar que seja semelhante
#lista = [item for item in lista if item != 2] -> remove todos os elementos iguais a 2 da lista (Lista é igual a item por item na lista se o item for diferente de 2)
#para copiar uma lista não é apenas "z1=z", isso apenas direciona a variável a demonstrar a lista z, para criar uma lista independente tem que usar "z1=z[:]" ou lista.copy()
#len(lista) para descobrir o tamanho da lista.
#del(z) deleta a lista z

"""
z=[0, 2, 4]
y=[]
z.append('teste')
z.insert(2, 'agua')
y=z.copy()
print(z)
z.pop(2)
print(z)
print(y)
print(len(z))
"""

"""
Pesquisando listas: WHILE ou FOR
Exemplo: procurar "c" na lista Z

z= ["a", "b", "c", "d", "e"]
for elemento in z:   #Para elemento em Z: vai realizar o comando para cada elemento de Z.
    if elemento == "c":
        print("Elemento encontrado!")
        break
    else:
        print("Elemento não encontrado!")

ou


z= ["a", "b", "c", "d", "e"]
b=str(input("Entre com uma letra: "))

if b in z:
    print("Elemento encontrado!")
else:
    print("Elemento não encontrado!")


for indice in range(len(z)): #len(z) retorna o tamanho da lista
    if z[indice]==b:
        print("O elemento encontrado está no índice %d" % indice)
    else:
        print("Elemento não encontrado!")
"""

"""
#Substituindo item na lista:
z=[1,'a', 5, 'b']
z[2]= 'v'
print(z) -> #[1, 'a', 'v', 'b']
"""

"""
#Adicionando elementos com "for inline"
teste = [x for x in range(10)]
print(teste) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

teste2 = [2*y for y in range(10)]
print(teste2)

lista1 = [t for t in teste if t%2 == 0] #-> adicionando estrutura
print(lista1)

lista2 = [r for r in teste if r>5]
print(lista2)
"""

#Tempo execução do for inline:

"""import time
a = time.time() #função time() retorna o tempo atual em segundos desde a época (1º de janeiro de 1970, 00:00:00 UTC)
lista = []
for x in range(1000000):
    lista.append(x)
print(time.time() - a)

a = time.time()
lista = [x for x in range(1000000)]
print(time.time() - a)
"""

"""É chamado o pacote "time" e depois usado a função ".time()" que verifica o horário atual da máquina em segundos.
Ele usa esta função pra pegar o horário de ínicio e final da função, depois subtrai pra saber quanto tempo demorou.
É feito uma lista onde é adicionado um número gigantesco de elementos para que seja possível passar um tempo grande o
bastante para ser possível comparar qual método de adição de elemento na lista é mais rápido.""" #o mais rápido 

"""Exercício de listas:
Faça um algoritmos que armazene 10 números inteiros
informados pelo usuário em uma Lista. Exiba como saída
o MAIOR numero dessa Lista.
OBRIGATÓRIO O USO DE LAÇO DE REPETIÇÃO PARA LEITURA DA LISTA."""

"""lista=[]
maiorN=0
for x in range (10):
    a=int(input("Digite um valor inteiro: "))
    lista.append(a)
    if a > maiorN:
        maiorN=a
print(lista)
print("O maior valor digitado é %d" % a)
"""

"""Crie uma Lista de números inteiros V[5]. Inicialize esse
vetor com números fixos e aleatórios (a sua escolha).
Exiba como saída a média dos valores desse vetor.
OBRIGATÓRIO O USO DE LAÇO DE REPETIÇÃO PARA LEITURA DA LISTA."""

"""
from random import randrange
a=[]
soma=0
media=0
for x in range(5):
    a.append(randrange(0,100))
print(a)

for x in range(len(a)):
    if x < len(a)-1:
        soma=soma+a[x]
    else:
        soma=soma+a[x]
        media=soma/len(a)
print("A soma dos números da lista é %d e a média da soma é %.2f" % (soma, media))
"""

"""Faça um algoritmo que leia 2 vetores A[10] e B[10].
A seguir, crie um vetor C que seja a intersecção de A com B
e mostre este vetor C.
Obs.: Intersecção é quando um valor estiver nos dois
vetores. Considere que não há elementos duplicados em
cada um dos vetores."""

"""
from random import randrange
a=[]
b=[]
c=[]
valora=0
valorb=0
for x in range(10):
    a.append(randrange(0, 20)) #Adiciona elemento aleatório entre 0 e 20 a lista
    b.append(randrange(0, 20))
print(a)
print(b)
for x in range(len(a)):
    for y in range(len(b)):
        if a[x]==b[y] and a[x] not in c:
                c.append(a[x])
        else:
             continue
print(c)"""

#Slicing (Fatiar listas para usar só a parte que queremos)
"""
p=[1,2,3,4,5,6, 7, 8, 9, 10]
print(p[1:5]) #:Result: [2, 3, 4, 5] ->  O primeiro Nº representa o índice do primeiro elemento a aparecer, o segundo o índice limitante (que não aparece)
print(p[:4]) #Result: [1, 2, 3, 4] -> O número o índice limitante (que não aparece)
print(p[-1]) #result: [-1] -> O sinal (-) Inverte a seleção do índice, começando pelo último valor.
"""

#Listas aninhadas: Lista que aparece como elemento de outra lista
"""b=["vida", 6.7, 5, [1, 2, 3]] #O quarto elemento é uma lista aninhada
print (b[3]) #Resultado: [1, 2, 3]
print(b[3][1]) #Resultado: 2 -> É colocado um segundo índice em colchetes pra acessar o índice do elemento desejado na lista aninhada."""
"""Os colchetes avaliam a sentença da esquerda para a direita, então o elemento no índice 3 será acessado primeiro.
Depois, como o elemento no índice 3 é outra lista, podemos acessar o elemento no índice 1, que é o número inteiro 2."""

#Matrizes
#Listas aninhadas podem ser usadas pra representar matrizes.

"""
a= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#ou podemos representar a mesma matriz como:
b=[[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]
"""

"""Matriz representada:
[1   2   3]
[4   5   6]
[7   8   9]"""

#Para acessar os valores da matriz:

"""for linha in range(3):
    for coluna in range(3):
        valor=a[linha][coluna]
        print(valor)"""

#Para acessar e vizualisar como uma matriz:

"""b=[[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]

for linha in range(len(b)):
    for coluna in range(len(b[linha])):
        print(b[linha][coluna], end="  ")
    print("\n")"""

"""Criar uma matriz, M, 10 x 15 cujos elementos são iguais
a somatória de sua linha com sua coluna (elemento =
linha + coluna)."""
"""
m=[]

for n_linha in range(10):
    linha=[]
    for n_coluna in range(15):
       linha.append(n_linha + n_coluna)
    m.append(linha)

for linha in range(len(m)):
    for coluna in range(len(m[linha])):
        print("%d" % m[linha][coluna], end="  ")
     
    print("\n")"""


"""Faça um programa que cria uma matriz M (5 x 10), sendo
que cada elemento é um inteiro gerado aleatoriamente.
Então, exiba a matriz completa e, na sequência, somente
os elementos da primeira coluna da matriz."""

"""
from random import *
matriz1=[]
for linha in range(5):
    Linha=[]
    for coluna in range(10):
        valor=randrange(0,101)
        Linha.append(valor)
    matriz1.append(Linha)

for linha in range(len(matriz1)):
    for coluna in range(len(matriz1[linha])):
        print("%d" % matriz1[linha][coluna], end="  ")
    print("\n")

print(matriz1[0])
"""

"""Faça um programa que cria uma matriz M (10 x 10),
sendo que cada elemento é um inteiro gerado
aleatoriamente no intervalo [0, 10]. Então, exiba a matriz
completa e a quantidade de incidências do número 3"""

"""from random import randrange
matriz=[]

for linha in range(10):
    Linha=[]
    for coluna in range(10):
        valor=randrange(0, 11)
        Linha.append(valor)
    matriz.append(Linha)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print("%d" % matriz[linha][coluna], end="  ")
    print("\n")

contagem=0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] == 3:
            contagem = contagem+1
        else:
            continue

print("A matriz tem o número 3 ocorrendo %d vezes" % contagem)"""


"""Faça um algoritmo que leia uma matriz M (populada com
números aleatórios) e exiba como saída o menor número
dessa matriz bem como o maior número."""

"""from random import randrange

M=[]
maior=0
menor=0
for linha in range(5):
    Linha=[]
    for coluna in range(5):
        elemento=randrange(0, 101)
        Linha.append(elemento)
        if maior==0 and menor==0:
            maior=elemento
            menor=elemento
        elif elemento > maior:
            maior=elemento
        elif elemento < menor:
            menor=elemento
        else:
            continue
    M.append(Linha)

for linha in range(len(M)):
        for coluna in range(len(M[linha])):
            print("%d" % (M[linha][coluna]), end="  ")
        print("\n")

print("Maior valor: %d" % (maior))
print("Menor valor: %d" % (menor))"""

"""Faça um programa que cria uma matriz M (2 x 2), sendo
que cada elemento deve ser digitado pelo usuário. Então,
faça seu programa criar outra matriz, N, que é resultante
do cálculo da multiplicação de cada elemento de M pelo
maior elemento da própria matriz M."""

"""M=[]
maior=0

for linha in range(2):
    Linha=[]
    for coluna in range(2):
        valor=int(input("Entre com o valor do elemento da matriz:  "))
        Linha.append(valor)
        if valor>maior:
            maior=valor
        else:
            continue
    M.append(Linha)

for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print("%d" % (M[linha][coluna]), end="  ")
    print("\n")

print("O valor de maior elemento é: %d" % maior)

resultante=[]

for linha in range(2):
    Linha=[]
    for coluna in range(2):
        Linha.append(M[linha][coluna]*maior)
    resultante.append(Linha)

for linha in range(2):
    for coluna in range(2):
        print("%d" % (resultante[linha][coluna]), end="  ")
    print("\n")"""

"""Escreva um programa que lê do teclado uma matriz de
números reais com quatro linhas e três colunas e imprime na
tela a matriz. Depois lê um valor digitado pelo usuário e
procura este valor na matriz. Se encontrar o valor, mostra
sua posição (ou índice). Se não encontrar este valor no vetor,
mostra na tela uma mensagem que não achou."""

"""
def teste(): #define nova função
    
    a=9
    b=6
    print(a+b)
    
teste()
"""

"""
def teste(a=3, b=8): #Se não receber parâmetros, a função é ativa com a=3 d b=8 por padrão
    soma=a+b
    return(soma) #retorno de forma a ter acesso ao valor fora da função

print(teste(5, 9))
"""

"""
def ehpar(num): #função precisa receber um parâmetro num
    a= num%2 == 0 #variavel local
    return(a)

print(ehpar(4))
print(ehpar(5))
"""

"""
a=5 #variavel global: variável do programa principal

def alteravalor():
    a=7 #variável local: variável acessada apenas dentro da função
    return(a)

print("Valor de a dentro da função: %d" % alteravalor())
print("Valor de a da variável global: %d" % a)
"""

"""
a=7

def alteravalor():
    global a
    a=7+8
    return(a) #ao fim da função, retorna a variável "a"

print("Valor de a global atualizado dentro da função: %d" % alteravalor())
"""

"""
def soma(a=2, b=3):
    soma=a+b

    return(soma)

print("Valor da soma na função:", soma())
print("Valor da soma na função:", soma(8, 9))
"""

"""
def teste(*args):
    print("args aceita tudo como variável: ", args)

teste(4, "a", 4j+3)

def teste2(**kwargs):
    print('kwargs é tudo que entra, mas sai como um dicionário: ', kwargs)

teste2(a=5, b="juan", c=25)
"""

def docteste(a=2, b=8):  #função para testar Docstring
    """Texto apenas para verificar o funcionamento da função DocString"""
    return(a+b)

"""
print(docteste.__doc__)
help(docteste)
"""

"""
a=lambda x: x**2 #lambda estabelece função simples em linha determinando paramêtro a variável (x)

print(a(4))
"""

"""
Escreva uma função com parâmetros que receba a base e a
altura de um triângulo e retorne sua área (A = base * altura / 2).
"""

"""
def areatriangulo(base, altura):
    area=(base*altura)/2
    return area

print(areatriangulo(int(input("Entre com a base do triângulo: ")), int(input("Entre com a altura do triângulo: "))))
"""

"""
Escreva uma função lambda que receba a base e a altura de um
triângulo e retorne sua área (A = base * altura / 2).

"""

"""
area=lambda base, altura: (base*altura)/2

print(area(int(input("Escreva a base do triângulo: ")), int(input("Escrea a altura do triângulo: "))))
"""

"""Escreva uma função lambda chamada par que receba um número
e retorne True se o número é par ou False caso contrário."""

"""
ehpar= lambda n: n%2 == 0
print(ehpar(int(input("Entre com valor para verificar se é par: "))))
"""

"""
notas=[]

def medianota(notas):
    media=(notas[0]+notas[1]+notas[2]+notas[3])/4
    return media

print("entre com 4 notas do aluno! \n")

for x in range(1,5):
    nota=input("Entre com a nota %d: " % x)
    if nota.strip()== "":
        nota=0
        notas.append(int(nota))
    else:
        notas.append(int(nota))

print(medianota(notas))
"""

"""Escreva uma função lambda que receba quatro parametros referente a
notas de atividades do aluno e retorne a media dessa 4 notas, caso
algumas notas não sejam atribuidas na chamada da função, atribuir como
padrão o valor zero para essa notas."""

"""notas=[]
medianota= lambda notas: (notas[0]+notas[1]+notas[2]+notas[3])/4

for x in range(1,5):
    nota=input("Entre com a nota %d: " % x)
    if nota.strip()== "":
        nota=0
        notas.append(int(nota))
    else:
        notas.append(int(nota))

print(medianota(notas))"""

"""Escreva uma função que receba uma lista de números e retorne o
maior e o menor número dessa lista."""

"""lista=[]

def maiormenor(lista):
    maior=0
    menor=0
    for x in range(len(lista)):
        if maior==0 and menor ==0:
            maior=lista[x]
            menor=lista[x]
        elif maior < lista[x]:
            maior = lista[x]
        elif menor > lista[x]:
            menor=lista[x]
    return(maior, menor)


for x in range(int(input("Quantos números quer colocar na lista? "))):
    valor=int(input("Coloque o valor %d: " % x))
    lista.append(valor)
print(lista)

print("O maior e o menor valor da lista são respectivamente %d e %d." % maiormenor(lista))
"""

"""Escreva uma função que receba uma lista e remova todos os valores
duplicados e retorne a lista sem elementos duplicados. Porém a
função não deve alterar a lista que recebeu como parâmetro."""

"""lista=[0, 4, 5, 7, 8, 4, 6, 1, 9, 0, 5, 3, 6, 8, 4]

def retiraduplicado(lista):
    aux=[]
    for x in range(len(lista)):
        if lista[x] not in aux:
            aux.append(lista[x])
        else:
            continue
    return aux

novalista=retiraduplicado(lista)
print(novalista)"""

"""Escreva uma função que receba uma lista de números inteiros e
retorne duas listas, uma com os números pares e outra com os
números impares."""

"""from random import randrange
lista=[]
for x in range(int(input("digite o tamanho desejado da lista: "))):
    valor=randrange(0, 101)
    if valor not in lista:
        lista.append(valor)
    else:
        while valor in lista:
            valor=randrange(0,101)
        lista.append(valor)

print(lista)

def parimpar(lista):
    par=[]
    impar=[]
    for x in range(len(lista)):
        if lista[x]%2==0:
            par.append(lista[x])
        else:
            impar.append(lista[x])
    return par, impar

print("Lista 1: %s\nLista 2: %s" % parimpar(lista))"""

"""Funções Recursivas: Funções que chamam a si mesmas, geralmente usadas para
resolver problemas que podem ser divididos em subproblemas menores do mesmo tipo.
Um exemplo clássico de função recursiva é o cálculo do fatorial de um número.
Outro exemplo é a sequência de Fibonacci, onde cada número é a soma dos dois anteriores."""

"""def fatorial(n):
    if n == 0 or n == 1:  # Caso base: fatorial de 0 e 1 é 1
        return 1
    else:
        return n * fatorial(n - 1)  # Chamada recursiva

# Exemplo de uso:
numero = int(input("Digite um número para calcular o fatorial: "))
print("O fatorial de %d é %d." % (numero, fatorial(numero)))"""

#String é uma cadeia de caracteres, podem ser criadas com aspas simples ou duplas.
#A diferença é que aspas simples permitem o uso de aspas duplas dentro da string e vice-versa.
#Strings são imutáveis, ou seja, não podem ser alteradas após serem criadas.
#Para modificar uma string, é necessário criar uma nova string com as alterações desejadas.

#ASCII - American Standard Code for Information Interchange, é um padrão de codificação de caracteres.
#ISO 8859-1 - Padrão de codificação de caracteres que inclui caracteres acentuados e símbolos especiais.
#Unicode - Padrão de codificação de caracteres que inclui caracteres de praticamente todos os idiomas do mundo (138k caracteres).
#UTF-8 - 8-bit Unicode Transformation format: Padrão de codificação compatível com ASCII e Unicode, é utilizado na web.

#Hexadecimal - Sistema de numeração base 16, utiliza os dígitos de 0 a 9 e as letras A a F para representar os valores de 10 a 15.
#Decimal - Sistema de numeração base 10, utiliza os dígitos de 0 a 9 para representar os valores.
#Octal - Sistema de numeração base 8, utiliza os dígitos de 0 a 7 para representar os valores.

"""#Exemplo de print de unicode:
print("\U0001f600") #onde U indica que é unicode e 0001f600 é o código do emoji de rosto sorridente.

#Para imprimir o valor ASCII/Unicode de um caractere, podemos usar a função ord():
print(ord('A'))  #Resultado: 65, que é o valor ASCII do caractere 'A'
print(ord('a'))  #Resultado: 97, que é o valor ASCII do caractere 'a'
print(ord('á'))  #Resultado: 225, que é o valor Unicode do caractere 'á'

#Para imprimir o caractere correspondente a um valor ASCII/Unicode, podemos usar a função chr():
print(chr(65))  #Resultado: 'A', que é o caractere correspondente ao valor ASCII 65
print(chr(97))  #Resultado: 'a', que é o caractere correspondente ao valor ASCII 97
print(chr(225))  #Resultado: 'á', que é o caractere correspondente ao valor Unicode 225"""

"""As aspas triplas ou "bloco de strings" permitem a criação de strings que ocupam múltiplas linhas,
enquanto as aspas simples e duplas são usadas para strings de uma única linha. Além disso, as aspas triplas
podem ser usadas para criar docstrings, que são strings de documentação para funções, classes e módulos."""

#Para inserir caracteres ilegais em uma string, podemos usar a barra invertida "\" como caractere de escape. Por exemplo:
#\n - nova linha ou new line
#\t - tabulação ou tab
#\\ - barra invertida ou backslash
#\' - aspas simples ou single quote
#\" - aspas duplas ou double quote
#\r - retorno de carro ou carriage return
#\b - backspace
#\f - avanço de página ou form feed
#\v - tabulação vertical ou vertical tab
#\ooo - caractere octal, onde o "ooo" é um número octal de 1 a 3 dígitos
#\xhh - caractere hexadecimal, onde o "hh" é um número hexadecimal de 1 a 2 dígitos
#\N{name} - caractere Unicode, onde "name" é o nome do caractere Unicode
#\uXXXX - caractere Unicode, onde "XXXX" é um número hexadecimal de 4 dígitos

#Strings são tuplas de caracteres.
#Tuplas são estruturas de dados que armazenam uma sequência de elementos, que podem ser de tipos diferentes, e são imutáveis.
#As tuplas são definidas usando parênteses () e os elementos são separados por vírgulas. Por exemplo:
#tupla = (1, 2, 3, 'a', 'b', 'c') #tupla com 6 elementos, sendo 3 inteiros e 3 strings.

#Índices:
#Podemos acessar cada caractere de uma string usando índices, assim como fazemos com listas e tuplas. Por exemplo:
#string = "Python" 

"""print(string[0])  #Resultado: 'P', que é o primeiro caractere da string
print(string[1])  #Resultado: 'y', que é o segundo caractere da string
print(string[-1])  #Resultado: 'n', que é o último caractere da string"""

#Slicing: O Fatiamento serve para extrairmos uma parte específica de uma string. Por exemplo:
"""Podemos fatiar uma string usando a sintaxe [início:fim:passo],
onde início é o índice do primeiro caractere a ser incluído, fim é o índice do primeiro caractere a ser excluído
e passo é o número de caracteres a serem pulados."""

#Exemplos:
#string = "Python"
"""print(string[1:3]) #Resultado: 'yt', que são os caracteres do índice 1 ao 2 (3 é excluído)
print(string[:4]) #Resultado: 'Pyth', que são os caracteres do índice 0 ao 3 (4 é excluído)
print(string[2:]) #Resultado: 'thon', que são os caracteres do índice 2 ao final da string
print(string[::2]) #Resultado: 'Pto', que são os caracteres do índice 0 ao final da string, pulando de 2 em 2 caracteres"""

#Strings são imutáveis, ou seja, não podemos alterar os caracteres de uma string após ela ter sido criada.
#Não podemos mudar "P" em "Python" para "J" apenas colocando string[0] = "J", pois isso geraria um erro.

#Para modificar uma string, precisamos criar uma nova string com as alterações desejadas. Por exemplo:
#s = "Python"
s_novo = "J" + s[1:] #Cria uma nova string com "J" no lugar de "P"

#Métodos para serem utilizados com strings:

#Capitalize() - Converte o primeiro caractere da string para maiúsculo e os demais para minúsculo.
#Upper() - Converte todos os caracteres da string para maiúsculo.
#Lower() - Converte todos os caracteres da string para minúsculo.
#Title() - Converte o primeiro caractere de cada palavra da string para maiúsculo.
#Swapcase() - Converte todos os caracteres maiúsculos para minúsculos e vice-versa.
#count(substring) - Retorna o número de ocorrências de uma substring na string.
#find(substring) - Retorna o índice da primeira ocorrência de uma substring na string. Retorna -1 se não encontrar.
#rfind(substring) - Retorna o índice da última ocorrência de uma substring na string. Retorna -1 se não encontrar.
#index(substring) - Retorna o índice da primeira ocorrência de uma substring na string. Gera um erro se não encontrar.
#rindex(substring) - Retorna o índice da última ocorrência de uma substring na string. Gera um erro se não encontrar.
#replace(old, new) - Substitui todas as ocorrências de uma substring por outra substring.
#islower() - Retorna True se todos os caracteres da string forem minúsculos. Caso contrário, retorna False.
#isupper() - Retorna True se todos os caracteres da string forem maiúsculos.
#isdigit() - Retorna True se todos os caracteres da string forem dígitos. Caso contrário, retorna False.
#isalpha() - Retorna True se todos os caracteres da string forem letras. Caso contrário
#split(sep) - Divide a string em uma lista de substrings, usando o separador sep. Se sep não for especificado, usa-se espaço em branco como padrão. Exemplo: "a b c".split() -> ['a', 'b', 'c']
#join(iterable) - Junta uma lista de strings em uma única string, usando a string como separador. Exemplo: "-".join(['a', 'b', 'c']) -> 'a-b-c'
#strip() - Remove os espaços em branco do início e do fim da string. Exemplo: "  a b c  ".strip() -> 'a b c'
#format() - Formata a string, substituindo os marcadores {} pelos valores passados como argumentos. Exemplo: "Olá, {}!".format("mundo") -> 'Olá, mundo!'
#len() - Retorna o tamanho da string, ou seja, o número de caracteres que ela possui. Exemplo: len("Python") -> 6




