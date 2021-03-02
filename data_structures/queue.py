import copy


class Element:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self):
        self.header = None
        self._len = 0
        self.end = None
    
    def append(self, elm):
        elm = copy.deepcopy(elm)
        if not self.header:
            self.header = elm
            self.end = elm
        else:
            self.end.next = elm
            self.end = elm
        self._len += 1

    def pop(self):
        if not self.header:
            raise ValueError("Queue Is Empty")
        print(self.header)
        self.header = self.header.next
        self._len -= 1

    def len(self):
        print(self._len)

    def __str__(self):
        if not self.header:
            return "[]"
        temp = self.header
        res = "["
        while True:
            if not temp.next:
                res += str(temp)
                break
            res += str(temp) + " ,"
            temp = temp.next
        res += "]"
        return res 


el1 = Element("afshin")
el2 = Element("nooooo")
el3 = Element("mapsaaaa")
el4 = Element(6273)
el5 = Element("zeidan")
el6 = Element(213.41)

queue1 = Queue()
queue1.append(el1)
queue1.append(el2)
queue1.append(el3)
queue1.append(el4)
queue1.append(el5)

print(queue1)
queue1.len()

queue1.append(el6)
queue1.pop()

print(queue1)
queue1.len()
