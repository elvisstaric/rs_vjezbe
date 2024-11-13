import numpy as np
class Krug:
    def __init__(self, r):
        self.r=r
    
    def opseg(self):
        return 2*self.r*np.pi
    
    def povrsina(self):
        return self.r**2*np.pi

krug=Krug(4)
print(f"Opseg kruga je {krug.opseg()}")
print(f"Površina kruga je {krug.povrsina()}")