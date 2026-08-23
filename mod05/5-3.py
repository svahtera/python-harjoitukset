list=[]

n=input("Syötä luku tai lopeta painamalla enter: ")
while n!="":
    list.append(str(n))
    n=input("Syötä luku tai lopeta painamalla enter: ")
print(max(list))