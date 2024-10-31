def count_vowels_consonants(tekst):
    vow=0
    con=0
    dic=dict()
    for i in tekst:
        if i in "aeiouAEIOU":
            vow=vow+1
        elif i == " " or i == "." :
            pass
        else:
            con=con+1
    dic["vowels"]=vow
    dic["consonants"]=con
    return dic

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))