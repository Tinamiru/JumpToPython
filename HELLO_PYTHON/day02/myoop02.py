class Xi:

    def __init__(self):
        self.money = 1000

    def steal(self, smoney):
        self.money += smoney


class Putin:

    def __init__(self):
        self.nuclear = 5000

    def alzheimer(self):
        self.nuclear -= 1


class JungEun:

    def __init__(self):
        self.missile = 10000

    def ssorau(self):
        self.missile -= 100


class Sungwoo(Xi, Putin, JungEun):

    def __init__(self):
        Xi.__init__(self)
        Putin.__init__(self)
        JungEun.__init__(self)

    
s = Sungwoo()

print(s.money)
s.steal(50)
s.steal(50)
s.steal(50)
print(s.money)

print()

print(s.nuclear)
s.alzheimer()
s.alzheimer()
s.alzheimer()
print(s.nuclear)

print()

print(s.missile)
s.ssorau()
s.ssorau()
s.ssorau()
print(s.missile)
