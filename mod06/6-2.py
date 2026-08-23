list=[]

n=input("Syötä luku tai lopeta painamalla enter: ")
while n!="":
    list.append(str(n))
    n=input("Syötä luku tai lopeta painamalla enter: ")
list.sort(reverse=True)

#print(list[0:5])
i=0
while i<5:
    print(list[i])
    i=i+1