string = ".(((...(((.........)))..((..(((......)))..((((.......)))).(((...)))...)).(((..(((.........)))))).))).."
string = "((...))...(((.....))).....((((....)).....((.....))))"
string = "((((.....)).((...))....))((((((....))...((...))))...((...))...(((.......)))))"
#         0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012
#                   1         2         3         4         5         6         7         8         9        10
tablica = []


def koniec(napis):   #= 1 gdy nie ma ju¿ innych struktur
    for znak in napis:
        if znak=="(":
            return 0
    return 1


def zamien(napis, drzewoarg):
    lista = []
    lista2= []
    p=0
    i=0
    while i < (len(napis)):
        if (napis[i]!="(" and napis[i]!=")"):
            p=i
            rz¹d=1
            while ((i<len(napis)) and (napis[i]!="(" and napis[i]!=")")) :
                if napis[i]!=".":
                    rz¹d+=1
                i+=1

            i-=1
            lista.append([p, i, rz¹d])

        i+=1

    for kr in lista:
        p = kr[0]-1
        liczbaP=0
        while(napis[p]=="(" and p>=0):
            p-=1
            liczbaP+=1
        k = kr[1] + 1
        liczbaK = 0
        while (k<len(napis) and napis[k] == ")"):
            k += 1
            liczbaK += 1
        liczba = liczbaK
        if liczba > liczbaP:
            liczba = liczbaP
        if liczba > 0:
            lista2.append([kr[0]-liczba, kr[1]+ liczba, kr[2]])

    #dobra lista2

    drzewo =[]
    zmiana = napis[:lista2[0][0]]
    ####
    for znak in zmiana:
        if (znak!="." and znak!="(" and znak!=")"):
            drzewo.append([int(znak)])
    ############
    for i in range (len(lista2)):
        petla = lista2[i]
        drzewo.append(petla[2])
        #znak = chr(petla[2])
        znak = str(petla[2])
        zmiana+=znak
        if (i<len(lista2)-1):
            nastêpna = lista2[i + 1]
            zmiana+=napis[petla[1]+1:(nastêpna[0])]
            for znak in (napis[petla[1]+1:(nastêpna[0])]):
                if (znak != "." and znak != "(" and znak != ")"):
                    drzewo.append([int(znak)])
        else:
            zmiana+=napis[petla[1]+1:]
            for znak in (napis[petla[1]+1:]):
                if (znak != "." and znak != "(" and znak != ")"):
                    drzewo.append([int(znak)])

    print("DRZEWO: ", drzewo)
    drzewoarg.append(drzewo);
    return(zmiana)

zamien(string, [])

zamien(zamien(string, []), [])
#

def liczba(char):
    return format(ord(char), "x")

def uproœæ(napis):
    tablica = []
    drzewo = []
    while(koniec(napis)!=1):
        print(napis)
        tablica.append(napis)
        napis = zamien(napis, drzewo)
    print(napis)
    tablica.append(napis)

    return[napis, drzewo]



print("==========")
x = uproœæ(string)

print("===========================================")
print("napis: ", x[0])
print("drzewo: ", x[1])

class wierzcho³ek:
    etykieta = ""
    dzieci = []
    def __init__(self, et, dz):
        etykieta = et
        dzieci = dz



class drzewo:
    korzeñ = [] # lista wierzcho³ków
    def _init_(self, k):
        korzeñ = k



def drzewo(drzewo):

    # na wejœciu takie coœ: [[1, 1, 1, 1, 1, 1], [3, 3, [1], [1]], [[3], 4]]

    nowedrzewo = drzewo
    nowedrzewo2=drzewo

    print(nowedrzewo)
    for i in range(1,len(nowedrzewo)):
        poprzednie = nowedrzewo[i-1]
        idx = 0;
        for j1 in range(0, len(nowedrzewo[i])):
            j=nowedrzewo[i][j1]

            #jesli jest list¹
            if(type(j)!=type([])):
                lista = []
                for k in range(idx, idx + j):
                    lista.append(poprzednie[k])
                w = wierzcho³ek(j, lista)
                nowedrzewo2[i][j1] = w;
                idx += j
            else:
                d=1
                tmpj=j[0]
                w = wierzcho³ek(j, [])
                nowedrzewo2[i][j1]=wierzcho³ek(j[0], []);
    return nowedrzewo2[-1]



drzewoD = drzewo(x[1])

print(type(drzewoD))
print(drzewoD[0])