
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
    

    def compression(self):
        pass

    
    def encode(self, text):
        """
        :param text: texto a codificar
        :return: texto codificado
        """
        codigo = {}
        arbol=HuffmanCoding.getTree(text)
        
        
        return arbol
        
        

    def getTree(self):
        """
        Retorna el árbol de Huffman.
        :return: árbol de Huffman
        """
        
        frecuencias = {}
        for car in self:
            if car in frecuencias:
                frecuencias[car] += 1
            else:
                frecuencias[car] = 1
                
    
                
        print(frecuencias)
        
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

        return heappop(priority_queue)
        
        
        
        
        # cola_prioridad = []
        # for car, freq in frecuencias.items():
            
        #     nodo = HuffmanBinaryTree(car, freq)
        #     heappush(cola_prioridad, nodo)

        # while len(cola_prioridad) > 1:
        #     nodo_izq = heappop(cola_prioridad)
        #     nodo_der = heappop(cola_prioridad)
        #     suma_freq = nodo_izq.freq + nodo_der.freq
        #     nodo_padre = HuffmanBinaryTree(None, suma_freq)
        #     nodo_padre.izq = nodo_izq
        #     nodo_padre.der = nodo_der
        #     heappush(cola_prioridad, nodo_padre)

        # return heappop(cola_prioridad)
    
        
        
        
        

    def getTable(self):
        """
        Retorna la tabla de codificación.
        :return: tabla de codificación
        """
       
    
    

    def getSummary(self):
        """
        Retorna el resumen de la codificación.
        :return: resumen de la codificación en formato string
        """
        raise NotImplementedError("Aún no implementado")
    
    
    

