class test:
    def len(self, arg1):
        if type(arg1) == list:
            self._len_list()
        else:
            self._len_others()

    def _len_list(self):
        print("list")

    def _len_others(self):
        print("others")


obj1 = test()
a = [1, 2]
obj1.len(a)

b ="s"
obj1.len(b)