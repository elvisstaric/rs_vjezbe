tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def brojanje_rijeci(tekst):
    rijecnik=dict()
    rijeci = tekst.split()
    for rijec in rijeci:
        rijec_cnt=0
        for riject_text in rijeci:
            if(riject_text==rijec):
                rijec_cnt=rijec_cnt+1
            rijecnik[rijec]=rijec_cnt
    return rijecnik

print(brojanje_rijeci(tekst))


