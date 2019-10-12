# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 07:54:24 2019

@author: Arunkumar Maniam Rajan
"""

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
    
class BST:
    PREORDER = 0
    INORDER = 1
    POSTORDER = 2
    OUTORDER = 4
    def __init__(self):
        self._root = None
        
    def put(self,key,val):
        self._root = self._put(self._root,key,val)
    
    def _size(self,node):
        if node is None: return 0
        return 1 + self._size(node.left) + self._size(node.right)
    
    def _put(self,node,key,val):
        if node is None : return Node(key,val)
        
        if key < node.key: 
            node.left = self._put(node.left,key,val)
        elif key > node.key:
            node.right = self._put(node.right,key,val)
        else:
            node.val = val
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node
    
    def printTree(self,order):
        if order == self.INORDER:
            self._printTreeInorder(self._root)
        elif order == self.OUTORDER:
            self._printTreeOutorder(self._root)
        elif order == self.POSTORDER:
            self._printTreePostorder(self._root)
        else:
            self._printTreePreorder(self._root)
        
    def _printTreeInorder(self,node):
        if node is None: return
        self._printTreeInorder(node.left)
        print(node.val)
        self._printTreeInorder(node.right)

    def _printTreePreorder(self,node):
        if node is None: return
        print(node.val)
        self._printTreePreorder(node.left)
        self._printTreePreorder(node.right)

    def _printTreePostorder(self,node):
        if node is None: return
        
        self._printTreePostorder(node.left)
        self._printTreePostorder(node.right)
        print(node.val)

    def _printTreeOutorder(self,node):
        if node is None: return
        self._printTreeOutorder(node.right)
        print(node.val)
        self._printTreeOutorder(node.left)
        
    def get(self,key):
        node = self._root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.val
        return None
        
    def _deleteMin(self,node):
        if node is None:
            return None
        if node.left is None:
            return node.right
        node.left = self._deleteMin(node.left)
        return node

    def deleteMin(self):
        self._root = self._deleteMin(self._root)
        
    def min(self,node):
        while node.left is not None:
            node = node.left
        return node
    
    def delete(self,key):
        self._root = self._delete(self._root,key)
        
    def _delete(self,node,key):
        if node is None: return None
        
        if key < node.val:
            node.left = self._delete(node.left,key)
        elif key > node.val:
            node.right = self._delete(node.right,key)
        else:
            if node.right is None: return node.left
            
            t = node
            node = self.min(t.right)
            node.right = self._deleteMin(t.right)
            node.left = t.left
        return node

    def floor(self,key):
        if self._root is None: return None
        
        x = self._floor(self._root,key)
        if x:
            return x.key
        return None

    def ceil(self,key):
        if self._root is None: return None
        
        x = self._ceil(self._root,key)
        if x:
            return x.key
        return None
    
    def _floor(self,node,key):
        if node is None: return None
        
        if node.key == key:
            return node
        elif key < node.key: 
            return self._floor(node.left,key)
        
        t = self._floor(node.right,key)
        if t is None:
            return node
        return t

    def _ceil(self,node,key):
        if node is None: return None
        
        if node.key == key:
            return node
        elif key > node.key:
            return self._ceil(node.right,key)
        
        t = self._ceil(node.left,key)
        if t is None:
            return node
        return t
    
    def rank(self,key):
        return self._rank(self._root,key)
            
    
    def _rank(self,node,key):
        if node is None:
            return 0
        if node.key < key:
            if node.left:
                return 1 + node.left.count + self._rank(node.right,key)
            return 1 + self._rank(node.right,key)
        elif node.key > key:
            return self._rank(node.left,key)
        else:
            if node.left:
                return node.left.count
            return 0
        
    def range_search(self,lo,hi):
        if self.contains(hi) : return self.rank(hi) - self.rank(lo) + 1
        return self.rank(hi) - self.rank(lo)
    
    def contains(self,key):
        return self._contains(self._root,key)
    
    def _contains(self,node,key):
        if node is None:
            return False
        
        if key > node.key:
            return self._contains(node.right,key)
        elif key < node.key:
            return self._contains(node.left,key)
        else: 
            return True
        
    def range_select(self,lo,hi):
        result = []
        self._range_select(self._root,lo,hi,result)
        return result
    
    def _range_select(self,node,lo,hi,result):
        if node is None:
            return 
        if node.val >= lo and node.val <= hi:
            result.append(node.val)
        if lo <= node.val:
            self._range_select(node.left,lo,hi,result)
        if hi >= node.val:
            self._range_select(node.right,lo,hi,result)
 
    def pathsum(self,target):
        return self._pathsum(self._root,0,target)
   
    def _pathsum(self,node,current_sum,target):
       if node is None:
           return current_sum == target
       return self._pathsum(node.left,node.val + current_sum,target) or self._pathsum(node.left,node.val+current_sum, target)
   
    def _lowestCommonAncestor(self,node,vals):
        if node is None:
            return None
        if node.val in vals:
            return node
        node.left = self._lowestCommonAncestor(node.left,vals)
        node.right = self._lowestCommonAncestor(node.right,vals)
        
        if node.left and node.right: return node
        
        if not node.left and not node.right: return None
        
        return node.right if node.right else node.left
        
    def lowestCommonAncestor(self,val1,val2):
        a = self._lowestCommonAncestor(self._root,[val1,val2])
        if a:
            return a.val
        return 0
        
        
        
            
        
                
        

tree = BST()
tree.put(10,10)
tree.put(11,11)
tree.put(9,9)

tree.put(21,21)
tree.put(20,20)
tree.put(29,29)
tree.put(30,30)
tree.put(31,31)
tree.put(39,39)
print(tree.ceil(8))
print(tree.rank(11))
print(tree.range_search(1,11))
print(tree.range_select(15,22))
print(tree.contains(30))
print(tree.pathsum(19))
print(tree.lowestCommonAncestor(11,9))
print(tree._root.count)
        