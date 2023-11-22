class Node:
    
    def __init__(self, value):
        self.value=value 
        self.izqda= None
        self.dcha = None


class Arbol:

    
    def insert(self, root, value):
        node = Node(value)
        if root is None:
            root = Node(value)
            return root
        else:
            if value < root.value:
                root.izqda = self.insert(root.izqda, value)
            else:
                root.dcha = self.insert(root.dcha, value)           
        
        return root
    
    def inorder(self, root):
        if root:
            self.inorder(root.izqda)
            print(root.value)
            self.inorder(root.dcha)
    
    def buscar(self, root, value):
        if root is None:
            return False
        elif root.value == value:
            return True
        elif root.value < value:
            return self.buscar(root.dcha, value)
        else:
            return self.buscar(root.izqda, value)        
    