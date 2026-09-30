class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self val):
        self.queue.append(val)
    def is_empty(self):
        return len(self.queue)==0
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    def front(self):
        if is self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    def display(self):
q=Queue()
print(q.is_empty())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()





