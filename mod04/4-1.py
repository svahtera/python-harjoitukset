numTest=bool(False)
while numTest==False:
    len=input("Syötä kuhan pituus (cm): ")
    len=len.replace(",", ".")
    try:
        float(len)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        len=float(len)
        numTest=True
if len < 37:
    print(f"Kuha on alamittainen, palauta se järveen. Alamitasta puuttuu {37-len}cm.")