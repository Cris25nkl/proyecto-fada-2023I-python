
import huffmanbinarytree

class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor: <Estudiantes>
    Version: <1>
    """
    def __init__(self):
        pass
    
    # Funcion para crear un arbol de huffman
#  -------------------------------------------------------------------------- #
  def crear_arbol(self, cadena):
    frecuencias = {}
    for caracter in cadena:
      if caracter in frecuencias:
        frecuencias[caracter] += 1
      else:
        frecuencias[caracter] = 1
    
    heap=[]
    
    for caracter, frecuencia in frecuencias.items():
      node = HuffmanBinaryTree(caracter, frecuencia)
      heappush(heap, (frecuencia, node))
      
    while len(heap) > 1:
      frecuencia1, node1 = heappop(heap)
      frecuencia2, node2 = heappop(heap)
      nodo_combinado = HuffmanBinaryTree(None, frecuencia1 + frecuencia2)
      nodo_combinado.left = node1
      nodo_combinado.right = node2
      heappush(heap, (frecuencia1 + frecuencia2, nodo_combinado))
      
    return heappop(heap)[1]

#  -------------------------------------------------------------------------- #

from heapq import heappush, heappop, heapify
    
    def getDiccionario(txt):
    
        frecuencia_letras = {}

        for letra in txt:
            if letra.isalnum() or letra in ['.',','] or letra.isspace():  # Verificar si es una letra o espacio
                if letra in frecuencia_letras:
                    frecuencia_letras[letra] += 1
                else:
                    frecuencia_letras[letra] = 1
            
        return frecuencia_letras

    def encode(self, text):
        """
        Codifica el texto.
        :param text: texto a codificar
        :return: texto codificado
        """
        raise NotImplementedError("Aún no implementado")

    def getTree(self):
        """
        Retorna el árbol de Huffman.
        :return: árbol de Huffman
        """
        
        
        raise NotImplementedError("Aún no implementado")

    def getTable(self):
        """
        Retorna la tabla de codificación.
        :return: tabla de codificación
        """
        raise NotImplementedError("Aún no implementado")

    def getSummary(self):
        """
        Retorna el resumen de la codificación.
        :return: resumen de la codificación en formato string
        """
        raise NotImplementedError("Aún no implementado")
