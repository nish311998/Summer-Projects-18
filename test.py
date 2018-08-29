
class Test():
    def __init__(self):
        self.x = 10
    def change(self):
        self.x = 5
        self.y = 5
    def change2(self):
        self.y = 10

t = Test()
t.change()
print(t.x)
print(t.y)
t.change2()
print(t.y)

