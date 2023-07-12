
import huffmanbinarytree as hbt
from heapq import heappush, heappop, heapify

class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor: <Estudiantes>
    Version: <1>
    """
    def __init__(self):
        pass
    

    #  -------------------------------------------------------------------------- #
    # Funcion para obtener el diccionario de frecuencias de un texto
        
    # def getDiccionario(txt):
        
    #     frecuencia_letras = {}

    #     for letra in txt:
    #         if letra.isalnum() or letra in ['.',','] or letra.isspace():  # Verificar si es una letra o espacio
    #             if letra in frecuencia_letras:
    #                 frecuencia_letras[letra] += 1
    #             else:
    #                 frecuencia_letras[letra] = 1
            
    #     return frecuencia_letras

    def compression(self):
        pass

    def encode(self, text):
        """
        :param text: texto a codificar
        :return: texto codificado
        """
        codigo = ""
        #nuevoArbol = crear_arbol(text)
        arbol = self.getTree(text)


        return codigo

    def getTree(self):
        """
        Retorna el árbol de Huffman.
        :return: árbol de Huffman
        """
        
        cadena = "Hola mundo"
        
        frecuencias = {}
        for caracter in cadena:
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
        
        heap=[]
        
        for caracter, frecuencia in frecuencias.items():
            node = hbt.HuffmanBinaryTree(caracter, frecuencia)
            heappush(heap, (frecuencia, node))

            while len(heap) > 1:
                frecuencia1, node1 = heappop(heap)
                frecuencia2, node2 = heappop(heap)
                nodo_combinado = hbt.HuffmanBinaryTree(None, frecuencia1 + frecuencia2)
                nodo_combinado.left = node1
                nodo_combinado.right = node2
                heappush(heap, (frecuencia1 + frecuencia2, nodo_combinado))
        return heappop(heap)[1]
        
        

    def getTable(self,arbol, codigo_actual="", codigos={}):
        """
        Retorna la tabla de codificación.
        :return: tabla de codificación
        """
        if arbol.key:
            codigos[arbol.key] = codigo_actual
        else:
            self.getTable(arbol.left, codigo_actual + "0", codigos)
            self.getTable(arbol.right, codigo_actual + "1", codigos)
        return codigos
    
    

    def getSummary(self):
        """
        Retorna el resumen de la codificación.
        :return: resumen de la codificación en formato string
        """
        raise NotImplementedError("Aún no implementado")
