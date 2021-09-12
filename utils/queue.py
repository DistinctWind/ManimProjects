class queue:
    def __init__(self):
        self.data = list()
        self.len = 0
    def put(self, x):
        self.data.append(x)
        self.len+=1
        return x
    def pop(self):
        res = self.data[0]
        del self.data[0]
        self.len-=1
        return res
    def empty(self):
        return self.len==0

class data_pack:
    def __init__(self, step, lin, col):
        self.step=step
        self.lin=lin
        self.col=col