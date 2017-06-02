
stringA =  ".(((...(((.........)))..((..(((......)))..((((.......)))).(((...)))...)).(((..(((.........)))))).))).."
stringB =  "((...))...(((.....))).....((((....)).....((.....))))"
string =   "((((.....)).((...))....))((((((....))...((...))))...((...))...(((.......)))))"
string1 =  "((.(.....)..((...))....))((((((....))...((...))))...(.....)...(((.......)))))"
#           0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012
#                     1         2         3         4         5         6         7         8         9        10
tablica = []


def koniec(napis):   # 1 gdy nie ma już innych struktur
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
            rząd=1
            while ((i<len(napis)) and (napis[i]!="(" and napis[i]!=")")) :
                if napis[i]!=".":
                    rząd+=1
                i+=1

            i-=1
            lista.append([p, i, rząd])

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
            następna = lista2[i + 1]
            zmiana+=napis[petla[1]+1:(następna[0])]
            for znak in (napis[petla[1]+1:(następna[0])]):
                if (znak != "." and znak != "(" and znak != ")"):
                    drzewo.append([int(znak)])
        else:
            zmiana+=napis[petla[1]+1:]
            for znak in (napis[petla[1]+1:]):
                if (znak != "." and znak != "(" and znak != ")"):
                    drzewo.append([int(znak)])

   # print("DRZEWO: ", drzewo)
    drzewoarg.append(drzewo)
    return(zmiana)

zamien(string, [])

zamien(zamien(string, []), [])
#


def uprość(napis):
    tablica = []
    drzewo = []
    while(koniec(napis)!=1):
        #print(napis)
        tablica.append(napis)
        napis = zamien(napis, drzewo)
    #print(napis)
    tablica.append(napis)

    return[napis, drzewo, tablica]


def ilePetli(string, rzad):
    x = uprość(string)
    drzewo=x[1]
    i=0
    for poziom in drzewo:
        for wierzchołek in poziom:
            if wierzchołek == rzad:
                i+=1
    return i




print("105==========")
x = uprość(string)

print("108==================================")
print(x[1])


print("125=======================")

print("115===========================================")



def metryka1(s1, s2): #procent niezgodnych pozycji
    if len(s1)!=len(s2):
        return 100
    d=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            d=d+1
    return 100*d/len(s1)


def metryka2(s1, s2):
    if len(s1)!=len(s2):
        return 100
    d=0
    for i in range (len(s1)):
       # print("liczba pętli rzędu" , i,  "wyonisi", ilePetli(s1, i) , ilePetli(s2, i))
        d+= (ilePetli(s1, i) - ilePetli(s2, i))**2

    d=d**(1/2)
    return d


def d(x, y, par):
    if (type(x)==type([]) and type(y)==type([])):      #odległość między listami - średnia odległość elementów
        od = 0
        for e in x:
            for e2 in y:
                od+=d(e, e2, par)
        return od/(len(x)*len(y))

    if type(x)==type([]):     #odległość między lista a elementem - średnia odległość od el. listy
        od = 0
        for e in x:
                od+=d(e, y, par)
        return od/(len(x))

    if type(y) == type([]):  # odległość między lista a elementem - średnia odległość od el. listy
        od = 0
        for e in y:
            od += d(e, x, par)
        return od / (len(y))
    #odległość między elementami:
    if par==1:
        return metryka1(x, y)
    if par==2:
        return metryka2(x, y)


def sasiad(lista, listaB, par): #zwraca drzewo podobieństwa między elementami listy
    #print(181, lista)
    min = d(lista[0], lista[1], par)
    #print("182", min)
    i1 = 0
    i2= 1
    for i in range(len(lista)):
        for j in range( i+1 , len(lista)):
            #print(187, d(lista[i], lista[j], par), min)
            if d(lista[i], lista[j], par) < min:
                min = d(lista[i], lista[j], par)
                i1=i
                i2=j
    lista2 = []
    lista3 = []

    for i in range(len(lista)):
        if (i!=i1 and i!=i2):
            lista2.append(lista[i])
            lista3.append(listaB[i])
    lista2.append([lista[i1], lista[i2]])
    lista3.append([listaB[i1], listaB[i2]])  #cmkemwfkewn
    #print(199, lista2, lista3)
    return [lista2, lista3]


def drzewo(lista, listaB, par):
    if len(lista)==1:
        return [lista, listaB]
    return drzewo(sasiad(lista, listaB, par)[0], sasiad(lista, listaB, par)[1], par)


s = drzewo([stringA, stringB, string, string1], [0, 1, 2, 3], 2)

print(214, s[0])
print(215, s[1])




print(152, metryka1(string, string1))

print(153, metryka2(string, string1))



################################
#EXAMPLE 1

_1arj_N = "..((((...((((......)))))))).."
_1uts_B = "((((((...((((......))))))))))"
_1uud_B = "((((((...((((......))))))))))"
_1uui_B = "((((((...((((......))))))))))"
_1anr_A = "(.(((....(((........))).))).)"

lista = [_1arj_N, _1uts_B , _1uud_B, _1uui_B, _1anr_A ]

s = drzewo(lista, [0, 1, 2, 3, 4], 1)
print(s[1])

s = drzewo(lista, [0, 1, 2, 3, 4], 2)
print(s[1])

_1f78_A=".((((.(((((......)))))))))."
_1f7f_A=".((((.(((((......)))))))))."
_1f6x_A=".((((.(((((......)))))))))."
_1f7h_A=".((((.(.(.(......).).)))))."

lista=[_1f78_A, _1f7f_A,_1f6x_A, _1f7h_A]

s = drzewo(lista, ["_1f78_A", "_1f7f_A","_1f6x_A", "_1f7h_A"], 1)
print(s[1])

s = drzewo(lista, ["_1f78_A", "_1f7f_A","_1f6x_A", "_1f7h_A"], 2)
print(s[1])


_1f79_A=".(((((.(((((....))))))))))."
_1f7g_A="((((((.(((((....)))))))))))"
_1f71_A=".(((((.(((((....))))))))))."
_1f6z_A="..((((.(((.(....).))))))).."

lista=[_1f79_A, _1f7g_A,_1f71_A, _1f6z_A]

s = drzewo(lista, ["_1f79_A", "_1f7g_A","_1f71_A", "_1f6z_A"], 1)
print(s[1])
s = drzewo(lista, ["_1f79_A", "_1f7g_A","_1f71_A", "_1f6z_A"], 2)
print(s[1])

_1bz3_A="(((((((...)))))))"
_1bz2_A="((((((.....))))))"
_1bzu_A="(((((.......)))))"
_1bzt_A="((((((.....))))))"

lista=[_1bz3_A, _1bz2_A,_1bzu_A, _1bzt_A]

s = drzewo(lista, ["_1bz3_A", "_bz2_A","_1bzu_A", "_1bzt_A"], 1)
print(s[1])

s = drzewo(lista, ["_1bz3_A", "_bz2_A","_1bzu_A", "_1bzt_A"], 2)
print(s[1])



_1cql_A="((((((..(.)((((..(((((..))))).).)))..))))))"
_1cq5_A="(((((...(..((((..(((((..))))).).))))..)))))"

#1 ile jest struktur

for i in range(10):
    print("_1cql_A ma " , ilePetli(_1cql_A, i) , "pętli rzędu ", i)
    print("_1cq5_A ma ", ilePetli(_1cq5_A, i) , "pętli rzędu ",  i)

#2 metryki

print(metryka1(_1cql_A, _1cq5_A))
print(metryka2(_1cql_A, _1cq5_A))


