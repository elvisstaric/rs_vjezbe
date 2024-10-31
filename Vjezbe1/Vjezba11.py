lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def grupiraj_po_partitetu(list):
    parni=[]
    neprni=[]
    rez={}
    for i in list:
        if(i%2==0):
            parni.append(i)
        else:
            neprni.append(i)
    rez["parni"]=parni
    rez["neparni"]=neprni
    return rez

print(grupiraj_po_partitetu(lista))
            