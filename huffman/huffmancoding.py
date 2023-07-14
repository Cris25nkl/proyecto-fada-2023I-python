
from huffmanbinarytree import HuffmanBinaryTree
from huffmandecoding import HuffmanDecoding
from heapq import heappush, heappop
import queue

class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor:  Cristian Florez
            Jesus Alberto Gil
            Andrés Cruz
            Jorge Augusto Estacio
    Version: <1>
    """
    def __init__(self):
        self.tree = None
        self.tabla = None
        self.text = None
        self.codigo = None
        self.compress = None
        pass
    

    def compression(self,len1,len2):
        compress = (1-(len1/(len2 * 256))) * 100
        return compress

    
    def encode(self, text):
        """
        :param text: texto a codificar
        :return: texto codificado
        """
        self.text = text
        
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
        
        print("Retorno del arbol\n",self.tree)
        
        # Se crea la tabla de codificación ----------------------------------------------------#
        self.tabla = self.recorrer_arbol(self.tree)
        
        print("Retorno de la tabla\n",self.tabla)
        codigo = "" 
        
        for cod in self.codigo:
            codigo += self.tabla[cod]
        
        self.codigo = codigo
            
        
        self.compress = self.compression(len(text),len(self.codigo))
    # ------------------------------------------------------------------------------------#
    
    def recorrer_arbol(self, nodo,codigo_actual="", tablas={}):
        # Se crea la tabla de codificación ----------------------------------------------------#
        
        if nodo.key is not None:
            tablas[nodo.key] = codigo_actual
        else:
            HuffmanCoding.recorrer_arbol(nodo.left, codigo_actual + "0", tablas)
            HuffmanCoding.recorrer_arbol(nodo.right, codigo_actual + "1", tablas)
        
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
    
    
    def contar_nodos_huffman(self, nodo):
        if nodo is None:
            return 0

        return 1 + self.contar_nodos_huffman(nodo.left) + self.contar_nodos_huffman(nodo.right)
    
    def obtener_profundidad_huffman(self, nodo):
        if nodo is None:
            return 0

        profundidad_izquierda = self.obtener_profundidad_huffman(nodo.left)
        profundidad_derecha = self.obtener_profundidad_huffman(nodo.right)

        return max(profundidad_izquierda, profundidad_derecha) + 1
    

    def getSummary(self):
        """
        Retorna el resumen de la codificación.
        :return: resumen de la codificación en formato string
        """
        nodos = self.contar_nodos_huffman(self.tree)
        profundidad = self.obtener_profundidad_huffman(self.tree)
        
        if self.tree is not None:
        
            return {
                "compresion" : self.compress,
                "Numero de nodos" : nodos,
                "Profundidad" : profundidad}
        else:
            return ""


decode = HuffmanDecoding() #Se crea una instancia pra importar la decodificacion.
encode = HuffmanCoding() #Se crea una instancia pra importar la codificacion.

encode.encode("mi pasion es programar") #Se codifica el texto.
    
    
    

