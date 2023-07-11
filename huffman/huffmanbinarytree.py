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
  
  def getNumberKey(self,node):
    if node.data.isalpha():
        return -1  # Si el nodo contiene un carácter, devuelve -1
    else:
        return node.data

  def __str__(self):
        return f'({self.key} {self.left} {self.right})' if self.left or self.right else str(self.key)
  
  def getLeft(self):
    if isinstance(self.left, HuffmanBinaryTree):
        return str(self.left)
    else: return None

  def getRight(self):
    if isinstance(self.right, HuffmanBinaryTree):
        return str(self.right)
    else: return None
