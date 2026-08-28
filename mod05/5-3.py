list=[]

n=int(input("Syötä luku tai lopeta painamalla enter: "))
while n!="":
    list.append(str(n))
    n=input("Syötä luku tai lopeta painamalla enter: ")
print(f'Suurin syöttämäsi luku on {str(max(list))}, pienin {str(min(list))}.')