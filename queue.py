class Queue:

    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.capacity = capacity
        self.Q = [None]*capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):
        if self.isFull():
            print('Full')
            return
        self.rear = (self.rear+1)%self.capacity
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("Inserted string is %s"%str(item))

    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return
        print("Value is %s"%self.Q[self.front])
        self.front = (self.front+1)%self.capacity
        self.size = self.size -1

def main():
    queue = Queue(30)
    queue.EnQueue(15)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.EnQueue(50)




if __name__ == "__main__":
    main()