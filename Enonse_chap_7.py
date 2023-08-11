repons= input("Ou vle antre yon tab iltiplikasyon, Peze W pou wi, N pou non \n")
while (repons=="w"):
    if (repons=="w"):
        continue
        #repons= input("Ou vle antre yon tab iltiplikasyon, Peze W pou wi, N pou non \n")
        nonb= input ("Antre nomb ki soti nan 1 rive nan 10  kou vle fe tab miltiplikasyon pou li a :\n")
        nonb=int(nonb)
        a=1
        if(int(nonb)>10):
            while not (int(nonb)<10):
                nonb=input("Nonb ou an siperye a 10, rantre yon lot:\n")
                if (int(nonb)<10):
                    while (a<=10):
                        print (nonb,"x",a,"=",int(nonb)*a)
                        a+=1
            
                else:
                    while (a<=10):
                        print (nonb,"x",a,"=",int(nonb)*a)
                        a+=1
    elif (repons=="n"):
        print ("mesi paske w te itilize program nan")
