
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime=ime
        self.prezime=prezime
        self.godine=godine
        self.ocjene=ocjene
    
    def prosjek(self):
        return (sum(self.ocjene)/len(self.ocjene))
        

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}]

studenti_objekti=[]
for student in studenti:
    st=Student(student["ime"], student["prezime"], student["godine"], student["ocjene"])
    studenti_objekti.append(st)

najbolji_student=None
max_prosjek = lambda st, st_naj, prosjek, naj : st if prosjek > naj else st_naj
for student in studenti_objekti:
    if(najbolji_student is None):
        najbolji_student=student
    else:
        najbolji_student= max_prosjek(student, najbolji_student, student.prosjek(), najbolji_student.prosjek())
print(najbolji_student.prosjek())