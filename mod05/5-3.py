list=[]

n=int(input("Syötä luku tai lopeta painamalla enter: "))
while n!="":
    list.append(str(n))
    n=input("Syötä luku tai lopeta painamalla enter: ")
print(f'Suurin syöttämäsi luku on {max(list)}, pienin {min(list)}.')