from queue import Queue

class MyStack:

    def __init__(self):
        self.queue_1=Queue()
        self.queue_2=Queue()

    def push(self, x: int) -> None:
        self.queue_2.put(x)
        while not self.queue_1.empty():
            self.queue_2.put(self.queue_1.get())
        self.queue_1,self.queue_2=self.queue_2,self.queue_1
    def pop(self) -> int:
        if not self.queue_1.empty():
            return self.queue_1.get()
        return -1 

    def top(self) -> int:
        if not self.queue_1.empty():
            return self.queue_1.queue[0]
        return -1

    def empty(self) -> bool:
        return self.queue_1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()