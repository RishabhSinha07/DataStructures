class two_stack:

    def __init__(self, size):
        self.list = [None]*size
        self.length = size
        self.size = 0
        self.front = 0
        self.last = size-1

    def full(self):
        return self.size == self.length

    def empty(self):
        return self.size == 0

    def push1(self, value):
        if two_stack.full(self):
            print("Stack full")
            return
        self.list[self.front]=value
        self.front = self.front + 1
        self.size = self.size + 1

    def push2(self, value):
        if two_stack.full(self):
            print("Stack full")
            return
        self.list[self.last] = value
        self.last = self.last - 1
        self.size = self.size + 1

    def print_stack(self):
        print(self.list)


if __name__ == "__main__":
    z = two_stack(10)
    z.push1(1)
    z.push2(91)
    z.push2(90)
    z.push2(89)
    z.push2(88)
    z.push1(2)
    z.push1(3)
    z.push1(4)
    z.push1(5)
    z.push1(6)
    z.push1(7)
    z.push1(7)
    z.push1(7)


    z.print_stack()
