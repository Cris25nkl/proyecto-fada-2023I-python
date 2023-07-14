import queue as Queue
#import HuffmanCoding as hc

class HuffmanDecoding:
    """
    Clase HuffmanDecoding
    Esta clase se encarga de decodificar un texto en base a un árbol de Huffman
    Autor:  Cristian Florez
            Jesus Alberto Gil
            Andrés Cruz
            Jorge Augusto Estacio
    Version: <1>
    """
    def __init__(self):
        pass

    def decode(self, text, tree):
        """
        Decodifica un texto en base a un árbol de Huffman.
        :param text: texto a decodificar
        :param tree: árbol de Huffman
        :return: texto decodificado
        """
        #puntero temporal
        temp = tree
        result = []

        for char in text:
            if char is '0':
                temp = temp.left
            else:
                temp = temp.right
            if temp.left is None and temp.right is None:
                result.append(temp.data)
                temp = tree
        print("".join(result))
    
