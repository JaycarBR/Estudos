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

arrayB[1, -1] - índice negativo também inverte a ordem do elemento na lista em array

arrayA[start : end] - slicing: start: início - end: elemento final (que não aparece), também pode adicionar o ": step" para passo

arrayA[1, 1:4] - fatiamento com dimensões, vai fatiar a lista dentro do elemento 1 da array
"""

