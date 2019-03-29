class rectangle:
    length=0
    bredth=0
    def __init__(self):
        self.length=40
        self.bredth=5
    def calc(self,a):
        r=self.length*self.bredth
        print(r)
a=rectangle()
b=rectangle()
b.calc(a)
