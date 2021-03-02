import copy


class Element:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.header = None
        self._index = 0
        self._len = 0
        self._now = None
    

    def __str__(self):
        if not self.header:
            return "List is Empty"
        res = "["
        temp = self.header
        while True:
            if not temp.next:
                res += str(temp.data)
                break
            else:
                res += (str(temp.data) + " ,")
            temp = temp.next
        res += "]"
        return res
        

    def append(self, elm):
        elm = copy.deepcopy(elm)
        if not self.header:
            self.header = elm
        else:
            temp = self.header
            while True:
                if not temp.next:
                    temp.next = elm
                    break
                temp = temp.next
        self._len += 1
        self._now = self.header


    def add_by_index(self, elm, index):
        elm = copy.deepcopy(elm)
        if not self.header:
            print("List is Empty")
        else:
            temp = self.header
            for i in range(index-1):
                if not temp.next:
                    raise ValueError("Out of Index")
                else:
                    temp = temp.next
            next = temp.next
            temp.next = elm
            elm.next = next
        self._len += 1
        self._now = self.header
        

    def __reverse(self, befor, temp):
        if not temp.next:
            self.header = temp
            self.header.next = befor
            self._now = self.header
            return True
        
        if LinkedList.__reverse(self, temp, temp.next):
            temp.next = befor
            return True
        

    def reverse(self):
        befor = None
        temp = self.header
        self._now = self.header
        return LinkedList.__reverse(self ,befor, temp)


    def remove(self, index):
        temp = self.header
        for i in range(index-1):
           temp = temp.next
        remove_item = temp.next
        next = remove_item.next
        temp.next = next

            
    def __iter__(self):
        return self
        

    def __next__(self):
        if not self._now:
            self._now = self.header
            raise StopIteration
        x = self._now
        if not self._now.next:
            self._now = None
        self._now = x.next
        return x
            
