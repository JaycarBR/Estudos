print("Oi, seja bem-vindo ao curso de Python!") #print: comando que exibe algo na tela

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
for elemento in z:
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
    a.append(randrange(0, 20))
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
