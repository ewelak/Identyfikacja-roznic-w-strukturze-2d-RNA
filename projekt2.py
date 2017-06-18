import os
from filecmp import dircmp
from pathlib import Path

from Bio.PDB import PDBParser


path = Path('C:/Users/Ewelina/PycharmProjects/Analiza danych 2/cw3/PLIKI PDB')
lista = list(path.glob('**/*.ent'))


print("HURA")
sciezka='C:/Users/Ewelina/PycharmProjects/Analiza danych 2/cw3/PLIKI PDB'
parser = PDBParser()
structure = parser.get_structure('X',
                                 'C:/Users/Ewelina/PycharmProjects/Analiza danych 2/cw3/PLIKI PDB/'
                                 + 'pdb1koc'.lower() + '.ent')
listaLancuchow=[]
listaLancuchow2=[]
listaRedundantnych=[]

def funkcja(string, tmplista):
    #filnam="C:\Us
    parser = PDBParser()
    structure = parser.get_structure('X', string)
    model=structure[0]
    for chain in model:
        tmplista.append([string[-8:-4],chain])


def długość(c1):
    i = 0
    for residue in c1:
        if((residue.get_resname()[2] == "A" and residue.get_resname()!=" NA") or residue.get_resname()[2]=="C" or residue.get_resname()[2]=="G" or residue.get_resname()[2]=="U"):
            i=i+1
    return i

def porownanieLancuchow(c1,c2):

    if długość(c1) != długość(c2):
        return 0

    i=0
    for residue in c1:
         j=0
         if((residue.get_resname()[2] == "A" and residue.get_resname()!=" NA") or residue.get_resname()[2] == "C" or residue.get_resname()[2] == "G" or residue.get_resname()[2] == "U"):  i = i + 1
         else: continue
         for residue1 in c2:
             if((residue1.get_resname()[2] == "A" and residue1.get_resname()!=" NA") or residue1.get_resname()[2] == "C" or residue1.get_resname()[2] == "G" or residue1.get_resname()[2] == "U"):  j = j + 1
             else: continue
             if (i == j):
                 if (residue.get_resname()[2] != residue1.get_resname()[2]):
                     return 0
                 break
    #print("===================================znalezione=================================")
    return 1

def przeszukiwanie():
    listaRed=[]
    lista=listaLancuchow[0]
    listaLancuchow.remove(lista)
    c1=lista[1]
    for l in listaLancuchow:
        c2=l[1]
        if(porownanieLancuchow(c1,c2)==1):
            listaRed.append(l)
    if(len(listaRed)>0):
        for l in listaRed:
            listaLancuchow.remove(l)
        listaRed.append(lista)
    listaRedundantnych.append(listaRed)


# for x in lista[:450]:
#     y=os.path.abspath(x)
#     funkcja(y, listaLancuchow)

def rozbicieNaLancuchy(a,b, sciezka):
    # filnam="C:\Us
    parser = PDBParser()
    structure = parser.get_structure('X', sciezka)
    model = structure[0]
    for chain in model:
        if(długość(chain)>=a and długość(chain)<=b):
            listaLancuchow.append([sciezka[-8:-4], chain])


def ileKlastrow(n):
    ile=0
    for chains in listaRedundantnychNOWA:
        if(len(chains)==n):
            ile+=1
    return ile

def ileKlastrowZJednej():
    suma=0
    for chains in listaRedundantnychNOWA:
        czyRozne = 0
        czast=chains[0][0]
        for el in chains:
            if(el[0]!=czast):
                czyRozne=1

        if(czyRozne==0):
            suma+=1

    return suma

def ileKlastrowZRoznych():
    suma=0
    for chains in listaRedundantnychNOWA:
        czast=chains[0][0]
        for el in chains:
            if(el[0]!=czast):
                suma+=1
                break
    return suma

for x in lista:
    y=os.path.abspath(x)
    rozbicieNaLancuchy(0,20,y)
#print(listaLancuchow)
while(len(listaLancuchow)!=0):
    przeszukiwanie()

# for chains in listaRedundantnych:
#     print(chains)

listaRedundantnychNOWA = []
for chain in listaRedundantnych:
    if chain!=[]:
        listaRedundantnychNOWA.append(chain)

dlugosci=[]
i=1
for chains in listaRedundantnychNOWA:
    dlugosci.append(len(chains))
    print(i,chains)
    i+=1

ileKlastrow1=[]
ileKlastrowZJednej1=0
ileKlastrowZRoznych1=0
for i in range(100):
    ileKlastrow1.append(ileKlastrow(i))
ileKlastrowZJednej1+=ileKlastrowZJednej()
ileKlastrowZRoznych1+=ileKlastrowZRoznych()
    #print("liczba klastrow o liczności",i,":", ileKlastrow(i))
# print("liczba klastrow, ileKlastrowZJednej())
# print(ileKlastrowZRoznych())
# print
print(ileKlastrow1)
for i in range(5):
    listaLancuchow=[]
    listaRedundantnych=[]
    for x in lista:
        y=os.path.abspath(x)
        rozbicieNaLancuchy(20*i+21,20*(i+1)+20,y)
    while (len(listaLancuchow) != 0):
        przeszukiwanie()

    listaRedundantnychNOWA = []
    for chain in listaRedundantnych:
        if chain != []:
            listaRedundantnychNOWA.append(chain)
    for i in range(100):
        ileKlastrow1[i]+=ileKlastrow(i)
    ileKlastrowZJednej1 += ileKlastrowZJednej()
    ileKlastrowZRoznych1 += ileKlastrowZRoznych()
print("lista liczności klastrow")
print(ileKlastrow1)
print(ileKlastrowZJednej1)
print(ileKlastrowZRoznych1)



###########################################################################
#                        listaRedundantnychNOWA                           #
###########################################################################


# for chains in listaRedundantnychNOWA:
#     print("============================")
#     for chain in chains:
#         print(chain)
#         print(długość(chain[1]))
#         i=0
#         for residue in chain[1]:
#             print(i, residue)
#             i+=1

for x in lista:
    y=os.path.abspath(x)
    rozbicieNaLancuchy(0,20,y)


