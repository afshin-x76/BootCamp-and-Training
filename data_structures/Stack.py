import copy

class Element:
    def __init__(self, data):
        self.data = data
        self.before = None

    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.header = None
        self._len = 0

    def add(self, elm):
        elm = copy.deepcopy(elm)
        if self.header:
            before = self.header
        else:
            before = None
        self.header = elm
        self.header.before = before
        self._len += 1
    
    def pop(self):
        if not self.header:
            raise ValueError("Stack is Empty")
        print(self.header)
        temp = self.header
        self.header = self.header.before
        temp.before = None
        self._len -= 1
        
    def len(self):
        print(self._len)

    def __str__(self):
        if not self.header:
            return "[]"
        res = "["
        temp = self.header
        while True:
            if not temp.before:
                res += str(temp)
                break
            else:
                res += str(temp) + " ,"
            temp = temp.before
        res += "]"
        return res
    
el1 = Element("Nooo")
el2 = Element("papa")
el3 = Element(218738)
el4 = Element("bad dog")
el5 = Element(788.23)

stack1 = Stack()
stack1.add(el1)
stack1.add(el2)
stack1.add(el3)
stack1.add(el4)

print(stack1)

stack1.pop()
stack1.add(el5)
print(stack1)
stack1.len()