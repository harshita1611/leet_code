class DLL:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=DLL(0,0)
        self.tail=DLL(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.mapp={}
        self.sz=0
    
    def add_to_head(self,node):
        temp=self.head.next
        node.next=  temp
        node.prev = self.head
        self.head.next=node
        temp.prev=node
    
    def deleteNode(self,node):
        if  node.prev and node.next:
            node.prev.next=node.next
            node.next.prev=node.prev

    def get(self, key: int) -> int:
        if key in self.mapp:
            node=self.mapp[key]
            res=node.val
            self.deleteNode(node)
            self.add_to_head(node)
            return res
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            node=self.mapp[key]
            node.val=value
            self.deleteNode(node)
            self.add_to_head(node)
        else:
            node=DLL(key,value)
            self.mapp[key]=node
            if self.sz<self.capacity:
                self.sz+=1
                self.add_to_head(node)
            else:
                lru_node = self.tail.prev
                del self.mapp[lru_node.key]
                self.deleteNode(lru_node)
                self.add_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
