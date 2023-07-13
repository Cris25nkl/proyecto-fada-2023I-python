class HuffmanBinaryTree:
  """
  Clase que implementa un árbol binario de Huffman
  Autor:<Estudiantes>
  """ 
  def __init__(self, key=None, left=None, right=None):
    """
    Constructor de la clase
    """
    self.key = None
    self.left = None
    self.right = None

  def __str__(self):
        return f'({self.key} {self.getLeft()} {self.getRight()})' if self.left or self.right else str(self.key)
  
  def getNumberKey(self):
        if isinstance(self.key, int):
            return self.key
        else: return -1 # Si el nodo contiene un carácter, devuelve -1
  
  def getLeft(self):
    if self.left is not None:
        return self.left
    else: return None

  def getRight(self):
    if self.right is not None:
        return self.right
    else: return None
