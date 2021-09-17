# -*-coding:utf-8 -*-

class Compare:
    def __init__(self, data, checkpoint):
        self.data = data
        self.checkpoint = checkpoint

    def compare(self):
        flag = None
        if isinstance(self.data, str):
            if self.checkpoint == self.data:
                flag = True
            else:
                flag = False
        elif isinstance(self.data, float):
            if self.data - float(self.checkpoint) == 0:
                flag = True
            else:
                flag = False
        elif isinstance(self.data, int):
            if self.data - int(self.checkpoint) == 0:
                flag = True
            else:
                flag = False
        return flag

