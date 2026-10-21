"""
Numpy é um pacote (pasta com módulos) que suporta arrays e matrizes, possuindo funções
mattemáticas para trabalhar com essas estruturas.

Podem ser usados em qualquer tarefa matemática: integral, diferenciação, interpolação,
extrapolação, entre outras. Podem ser usados para algebra linear, transfrmadas de fourrier
e geração de números aleatórios.

Podem até substituir o uso de matlab se combinada com Matplotlib e SciPy.

NumPy é utilizado por Processamento de Imagem e Computação Gráfica.
Imagens no computador são representadas como Arrays Multidimensionais de números.
O NumPy  fornece algumas excelentes funções de biblioteca para manipulação de imagens.

NumPy é utilizado por Machine Learning
Ao escrever algoritmos de Machine Learning, são realizados vários cálculos numéricos em Array.
EX: multiplicação de Arrays, transposição, adição, etc.
O NumPy fornece uma excelente biblioteca para cálculos fáceis (em termos de
escrita de código) e rápidos (em termos de velocidade).

Os Arrays NumPy são usados para armazenar os dados de treinamento, bem
como os parâmetros dos modelos de ML.

Em Python usamos listas para tratar vetores e matrizes, mas elas são lentas para processar.
O NumPy fornece um objeto array que é até 50x mais rápido que o Python tradicional.

Os arrays são muito frequentemente usados em ciência de dados, onde
velocidade e recursos são muito importantes.

Os arrays NumPy são armazenados em um lugar contínuo na memória - ao
contrário das listas, para que os processos possam manipulá-los de forma muito
eficiente. Esse comportamento é chamado de localidade de referência em ciência da
computação. Esta é a principal razão pela qual o NumPy é mais rápido do que as listas.
"""
#Para usar o Numpy:

"""import numpy as np

ou

import numpy

print(numpy.__version__) para verificar a versão
"""

"""podemos passar uma lista, tupla ou qualquer objeto semelhante a matriz
no método array() e ele será convertido em um objeto do tipo ndarray.

Elementos dos arrays são acessados iguais as listas."""

#Arrays em Numpy:

"""import numpy as np
arr= np.array([1, 2, 3, 4, 5]) #cria algo como uma lista, mas sem vírgula - 1 Dimensão (vetor)
print(arr)
print(type(arr))    #'numpy.ndarray'

arr2= np.array([[1, 2], [3, 4]]) #2Dimensções: array 2D p/ representar matrizes
print(arr2)
print(type(arr2)) 

arr3= np.array((1, 2, 3, 4, 5)) 
print(arr3)
print(type(arr3))

arr4= np.array([[1, 2], [3, 4, 5]], dtype=object) #só funciona se definir os elementos como objeto, não aceita como matriz com um elemento a menos.
print(arr4)

arr5= np.array(47) #0 Dimensão (número escalar)
print(arr5)
print(type(arr5))"""

"""
3-D: Um array que tem arrays 2D como seus elementos é chamado de array 3D. Estes são
frequentemente usados para representar um tensor de 3a ordem."""

#Descobrindo a dimensão de um array:

"""a = np.array([1, 2, 3])
print(a.ndim) #print: 1 (dimensão)"""

"""Os arrays podem ser acessados igual listas ou separando dimensões por vírgula dentro dos colchetes:
arrayA[2][1] - elemento de índice 1 do elemento 2 da array
ou
arrayA[2, 1] - elemento de índice 1 do elemento 2 da array

arrayB[1, -1] - índice negativo sobre o elemento 1 da array, também inverte a ordem do elemento na lista em array

arrayA[start : end] - slicing: start: início - end: elemento final (que não aparece), também pode adicionar o ": step" para passo

arrayA[1, 1:4] - fatiamento com dimensões, vai fatiar a lista dentro do elemento 1 da array
"""

#Tipos de dados em Numpy:

"""
i - integer
b - boolean
u - unsigned integer (inteiro sem sinal)
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type (void)

dtype() - para descobrir o tipo de dado em Numpy

para criar um array com tipo específico:

arr = np.array([1, 2, 3, 4], dtype='S')  -   Criou uma array de strings com números

Os tipos i (inteiro), u (inteiro sem sinal, f (número com ponto flutuante),
S (string de tamanho fixo) e U (unicode com tamanho fixo) permitem definir o tamanho em bytes.

Exemplos:

    i4  - inteiro de 4 bytes, equivalente a int32
    u4  - inteiro de 4 bytes, equivalente a int32
    f8  - número de 8 bytes, equivalente a float64
    S5  - até 5 bytes por elemento
    U5  - Até 5 caracteres Unicode por elemento
"""
    
#Exemplo 2:
"""   import numpy as np

    arr = np.array([1, 2, 3, 4], dtype='S5')

    print(arr)
    print(arr.dtype)"""

#Saída:
"""    
    [b'1' b'2' b'3' b'4']
    |S5
"""
"""Ao escrever dtype='S5', você pede que os valores sejam armazenados como sequências de bytes,
não como inteiros. Assim, 1 passa a ser representado como b'1', e cada posição tem capacidade para até 5 bytes.
O prefixo b identifica uma sequência de bytes.

O resultado |S5 significa:
    |: a ordem dos bytes não se aplica a esse tipo;
    S: sequência de bytes;
    5: tamanho reservado de 5 bytes por elemento."""

#copy() - Para copiar uma array, senão apenas cria uma referência
#.shape - retorna uma tupla com cada índice tendo os números correspondentes em cada dimensão. Exemplo: (2, 3) = 2 elementos (lista) com 3 elementos em cada
#.reshape - alterar a forma de uma array, número de elementos ou dimensões.

"""arr = np.array([1, 2, 3, 4, 5, 6])
aux= arr.reshape(3, 2) #3 dimensões com 2 elementos cada: [[1, 2], [3, 4], [5, 6]]"""

#Flattening (reduz qualquer array multidimensional à uma dimensão)

"""arr = np.array([[1, 2], [3, 4], [5, 6]])
arr2=arr.reshape(6)"""

"""Métodos Array:
.sort() ordena os arrays em ordem alfabética ou numérica"""

"""
#Funções Básicas
    #Criando matrizes:
        #np.ones((3, 2)) - cria matriz de 1 com 3 linhas e 2 colunas
        #np.zeros((3, 2)) - cria matriz de 0 com 3 linhas e 2 colunas
        #np.random.rand(3, 2)
    #Soma escalar
        data=np.array([1, 2])
        ones=np.ones([2, dtype=int])
        data + ones - #saída = [2,3]"""
    #Subtração escalar a - b
    #Multiplicação escalar a * b
    #Divisão escalar a / b

    #Soma de matrizes de diferentes tamanhos
"""     a=[[1,2], [3,4]]
        b=[1, 1]
        a + b = [[1,2], [3,4]] + [1, 1]  =  [[1,2], [3,4]]  +  [[1,1], [1,1]]
"""

#Produto escalar = [a b] * [x y] = ax + by - multiplicacao entre 2 vetores que resulta em um número real.
"""import numpy as np
data= np.array([1, 2])
data2= np.array([3, 4])
x= data.dot(data2)          #dot() pode ser para multiplicação de matrizes
print(x)"""

"""data = np.array([[1, 2], [3, 4]])
data2 = np.array([[5, 6], [7, 8]])
x = data.dot(data2)"""
# x = [[1*5 + 2*7] [1*6 + 2*8] [3*5 + 4*7] [3*6 + 4*8]] = [[19 22] [43 50]]

#cross() - produto vetorial resulta em um terceiro vetor ortogonal aos 2 vetores. - calculado por meio de dterminante (IJK)
"""
i = (1, 0, 0)
j = (0, 1, 0)
k = (0, 0, 1)"""

#.transpose() ou .t() = tomba a matriz de pé pra esquerda ou levanta para a direita
#exemplo: [[1,2] [3,4] [5,6]] -> [[1, 3, 5] [2, 4, 6]]

#numpy.linalg,inv() - matriz inversa
"""
matriz * matriz inversa = matriz identidade  
matriz identidade=[[1 0] [0 1]] 
matriz inversa = [[a b] [c d]]
"""

#.max() - maior elemento de matriz ou vetor
#.min() - menor elemento de matriz ou soma
#.sum() - soma de todos os elementos de matriz ou vetor

#máximo, mínimo ou soma por linha ou coluna: adicionar axis (0 ou 1):
#data.max(axis=0) - coluna
#data.max(axis=1) - linha

#números aleatórios em numpy:    módulo "random" do numpy
#np.random.rand() - retorna número real entre 0 e 1.
#np.random.randint(n) - retorna número aleatório inteiro entre 0 e n