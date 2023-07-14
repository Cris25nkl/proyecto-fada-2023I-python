
from huffmanbinarytree import HuffmanBinaryTree
from heapq import heappush, heappop
import queue

class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor: <Estudiantes>
    Version: <1>
    """
    def __init__(self):
        pass
    

    def compression(self,len1,len2):
        compress = (1-(len1/len2)) * 100
        return compress

    
    def encode(self, text):
        """
        :param text: texto a codificar
        :return: texto codificado
        """
        
        if text is "":
            return ""
        
        len1 = len(text)
        
        frecuencias = {}
        for car in text:
            if car in frecuencias:
                frecuencias[car] += 1
            else:
                frecuencias[car] = 1
                
    
                
        print(frecuencias)
        
        
        # Se crea el arbol de Huffman ---------------------------------------------------------#
        priority_queue = []
        for character, frequency in frecuencias.items():
            node = HuffmanBinaryTree(character, frequency)
            heappush(priority_queue, node)

        while len(priority_queue) > 1:
            right_child = heappop(priority_queue)
            left_child = heappop(priority_queue)
            
            
            parent_frequency = left_child.freq + right_child.freq
            parent_node = HuffmanBinaryTree(parent_frequency, parent_frequency)
            parent_node.left = left_child
            parent_node.right = right_child
            heappush(priority_queue, parent_node)

        self.tree =  heappop(priority_queue)
        
        # Se crea la tabla de codificación ----------------------------------------------------#
        self.tabla = self.recorrer_arbol(self.tree)
        
        
        codigo = "" 
        
        for cod in self.codigo:
            codigo += self.tabla[cod]
        
        self.codigo = codigo
            
        
        self.compress = self.compression(len(text),len(self.codigo))
    # ------------------------------------------------------------------------------------#
    
    def recorrer_arbol(self, codigo_actual="", tablas={}):
        # Se crea la tabla de codificación ----------------------------------------------------#
        
        if self.tree.key is not None:
            tablas[self.tree.key] = codigo_actual
        else:
            HuffmanCoding.recorrer_arbol(self.tree.left.key, codigo_actual + "0", tablas)
            HuffmanCoding.recorrer_arbol(self.tree.right.key, codigo_actual + "1", tablas)
        
        return tablas
    #------------------------------------------------------------------------------------#

    def getTree(self):
        """
        Retorna el árbol de Huffman.
        :return: árbol de Huffman
        """
        return self.tree
    
        
        
        
        

    def getTable(self):
        """
        Retorna la tabla de codificación.
        :return: tabla de codificación
        """
       
        return self.tabla
    

    def getSummary(self):
        """
        Retorna el resumen de la codificación.
        :return: resumen de la codificación en formato string
        """
        if self.tree is not None:
        
            return {
                "compresion" : self.compress,
                "Numero de nodos" : "por deducir",
                "Profundidad" : "por deducir"}
        else:
            return ""

       
    
    
    

