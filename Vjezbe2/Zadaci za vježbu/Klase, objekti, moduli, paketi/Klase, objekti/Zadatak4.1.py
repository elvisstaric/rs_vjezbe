import datetime

#1.
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka=marka
        self.model=model
        self.godina_proizvodnje=godina_proizvodnje
        self.kilometraza=kilometraza
    
    def ispis(self):
        print(self.marka, self.model, self.godina_proizvodnje, self.kilometraza)
    
    def starost(self):
        print(f"Auto je staro {datetime.date.today().year-int(self.godina_proizvodnje)} godine")
        

auto=Automobil("VW", "Golf 8", "2021", "10000")
auto.ispis()
auto.starost()




