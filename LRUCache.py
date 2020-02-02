class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.lruListHead = None
        self.lruListTail = None
        self.capacity = capacity
        self.size = 0
        

    def get(self, key):
        if key in self.cache:
            self.moveToHead(self.cache[key])
            return self.cache[key].data
        
        return -1
        

    def put(self, key, data):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            if self.capacity == self.size:
                self.evictLeastRecentlyUsed()
                
                
            node = DoublyLinkedListElem(key,data)
            self.insertAtHead(node)
            self.cache[key] = node
            self.size += 1
        else:
            self.cache[key].data = data
            self.moveToHead(self.cache[key])
               
    
    def evictLeastRecentlyUsed(self):
        if not self.lruListHead:
            return
        
        node = self.lruListTail
        
        if self.lruListTail == self.lruListHead:
            self.lruListTail = None
            self.lruListHead = None
        else:
            self.lruListTail = self.lruListTail.prev
            self.lruListTail.next = None
        
        node.next = None
        node.prev = None
        
        del self.cache[node.key]
        
        self.size -= 1
        
    def insertAtHead(self, node):
        if not node:
            return
        
        if self.lruListHead is None:
            self.lruListHead = node
            self.lruListTail = node
        else:
            node.next = self.lruListHead
            self.lruListHead.prev = node
            self.lruListHead = node
        
    def moveToHead(self, node):
        
        if node == self.lruListHead:
            return
        else:
            #detach Node
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.lruListTail = node.prev
                self.lruListTail.next = None
            node.next = None
            node.prev = None
            self.insertAtHead(node)
        
class DoublyLinkedListElem(object):
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.next = None
        self.prev = None
