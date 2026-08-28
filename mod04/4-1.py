iLen=int(input("Syötä kuhan pituus (cm): "))
if iLen < 37:
    print(f"Kuha on alamittainen, palauta se järveen. Alamitasta puuttuu {37-iLen}cm.")