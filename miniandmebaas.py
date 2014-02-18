#!/usr/bin/env python
# -*- coding: utf8 -*-

raamat=[]
autor=[]
v2ljalaskeaasta=[]

def lisamine():
    raamat_sisestus=raw_input("Sisesta raamat: ")
    autor_sisestus=raw_input("Sisesta autor: ")
    v2ljalaskeaasta_sisestus=raw_input("Sisesta v2ljalaskeaasta: ")
    if not raamat_sisestus and not autor_sisestus and not v2ljalaskeaasta_sisestus: 
        raamat_sisestus="--"
        autor_sisestus="--"
        v2ljalaskeaasta_sisestus="--"
    
    raamat.append(raamat_sisestus)
    autor.append(autor_sisestus)
    v2ljalaskeaasta.append(v2ljalaskeaasta_sisestus)

def vaatamine():
    if not raamat and not autor and not v2ljalaskeaasta:
        print ("Pole kirjeid mida vaadata")
    i=0
    for x,y,z in zip(raamat,autor,v2ljalaskeaasta):
        print(str(i)+":"+"  "+ x + ", " + y + ", " + z + ".")
        i+=1
        
def kustutamine():
    if not raamat and not autor and not v2ljalaskeaasta:
        return ("Pole kirjeid mida kustutada")
    else:
        kirje=raw_input("Sisesta kirje number mida kustutada: ")

        if kirje.isdigit():
            kirje=int(kirje)
            
            if kirje>len(raamat)-1:
                return ("Sellist kirjet pole")
            else:
                raamat.pop(kirje)
                autor.pop(kirje)
                v2ljalaskeaasta.pop(kirje)
        else:
            return ("Sisesta number")

while True:
    valik=raw_input("1=Lisa kirje\n2=Kustuta kirje\n3=Vaata kirjeid\n4=V2lju\nVali: ")
    if valik=="1":
        print (lisamine())
    elif valik=="2":
        print (kustutamine())
    elif valik=="3":
        print (vaatamine())
    elif valik=="4":
        exit()
    else:
        print ("Selline valik puudub")
            












