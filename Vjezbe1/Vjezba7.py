passw=input("Unesite loziknu: ")

def passwrdCheck(passw):
    hasNum=False
    hasUpper=False
    for i in passw:
        if i.isnumeric():
            hasNum=True
        elif i.isupper():
            hasUpper=True

    if len(passw) < 8 or len(passw) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
    if  hasNum==False or hasUpper==False:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
    if "password" or "lozinka" in passw:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")

passwrdCheck(passw)