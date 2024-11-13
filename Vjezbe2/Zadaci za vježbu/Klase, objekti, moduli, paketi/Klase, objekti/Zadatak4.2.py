class Kalkulator:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def zbroj(self):
        return self.a+self.b
    def oduzimanje(self):
        return self.a-self.b
    def mnozenje(self):
        return self.a*self.b
    def djeljenje(self):
        return self.a/self.b
    def potenciranje(self):
        return self.a**self.b
    def korijen(self):
        return self.a**(1/self.b)
kalk= Kalkulator(9,2)
print(kalk.zbroj())
print(kalk.oduzimanje())
print(kalk.mnozenje())
print(kalk.djeljenje())
print(kalk.potenciranje())
print(kalk.korijen())