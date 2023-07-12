
import huffmanbinarytree as hbt

class HuffmanCoding:
    """
    Clase HuffmanCoding
    Esta clase se encarga de codificar un texto en base a un árbol de Huffman
    Autor: <Estudiantes>
    Version: <1>
    """
    def __init__(self):
        pass
    
    
    
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
        
        arbol1 = hbt.crear_arbol(text)
        
        
        
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
