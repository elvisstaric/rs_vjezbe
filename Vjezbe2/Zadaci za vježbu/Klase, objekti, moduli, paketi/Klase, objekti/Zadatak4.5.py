class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime=ime
        self.pozicija=pozicija
        self.placa=placa
    def work(self):
        print(f"Radim na poziciji {self.pozicija} za placu od {self.placa}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department=department
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
    def give_raise(self, radnik, povecanje):
        radnik.placa+=povecanje

radnik=Radnik("Pero", "Pozicija1", 1000)
manager=Manager("Ivan", "Manager", 2000, "Odjel1")

radnik.work()
manager.work()
manager.give_raise(radnik, 100)
radnik.work()