raamatud= {0:{"raamat":"dsh",
           "autor":"hffh",
           "väljalaskeaasta":"dfhdfh"
}}

def lisamine():
    global raamatud
    
    raamat_sisestus=raw_input("Sisesta raamat: ")
    autor_sisestus=raw_input("Sisesta autor: ")
    väljalaskeaasta_sisestus=raw_input("Sisesta väljalaskeaasta: ")
    if not raamat_sisestus:
        raamat_sisestus="--"
    if not autor_sisestus:    
        autor_sisestus="--"
    if not väljalaskeaasta_sisestus:    
        väljalaskeaasta_sisestus="--"
    index = len(raamatud)

    uus_index = len(raamatud)
    
    while True:
        if uus_index in raamatud:
            uus_index+=1
        else:
            break
    
    raamatud[uus_index] = {"raamat":raamat_sisestus, "autor":autor_sisestus, "väljalaskeaasta":väljalaskeaasta_sisestus}
def vaatamine():
    global raamatud
    
    for each in raamatud:
        print str(each),raamatud[each]
        
def kustutamine():
    kirje=raw_input("Sisesta kirje number mida kustutada: ")
    
    if kirje.isdigit():
        kirje=int(kirje)
                            
        if kirje>len(raamatud):
            return ("Sellist kirjet pole")
        else:
            del raamatud[kirje]
    else:
        print "Sisesta number!"
    

def muuda():
    kirje = int(raw_input("Kirje id: "))
    võti = raw_input("Võti: ")
    väärtus = raw_input("Väärtus: ")
    raamatud[kirje][võti] = väärtus

while True:
    valik=raw_input("1=Muuda\n2=Lisa kirje\n3=Kustuta kirje\n4=Vaata kirjeid\n5=Välju\nVali: ")
    if valik=="1":
        print muuda()
    elif valik=="2":
        print lisamine()
    elif valik=="3":
        print kustutamine()
    elif valik=="4":
        print vaatamine()
    elif valik=="5":
        exit()
    else:
        print "Selline valik puudub"
           













