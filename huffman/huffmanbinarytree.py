from heapq import heappush, heappop, heapify

class HuffmanBinaryTree:
  
  """
  Clase que implementa un árbol binario de Huffman
  Autor:<Estudiantes>
  """ 
  def __init__(self, key, frecuencia):
    """
    Constructor de la clase
    """
    self.key = key
    self.frecuencia = frecuencia
    self.left = None
    self.right = None
    
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
  
  
def getNumberKey(self,node):
    """
    Retorna el valor de la llave, 
    si es un string retorna -1, si es un 
    numero retorna el numero.
    """
    if node.data.isalpha():
        return -1  # Si el nodo contiene un carácter, devuelve -1
    else:
        return node.data
      
def getLeft(self):
    """
    Retorna el hijo izquierdo del arbol.
    """
    raise NotImplementedError("Aún no implementado")
  

def getRight(self):
    """
    Retorna el hijo derecho del arbol.
    """
    raise NotImplementedError("Aún no implementado")
  
  
  
