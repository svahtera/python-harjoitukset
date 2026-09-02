list=[]

n=input("Syötä luku tai lopeta painamalla enter: ")
while n!="":
    list.append(int(n))
    n=input("Syötä luku tai lopeta painamalla enter: ")
list.sort(reverse=True)

for i in range(5):
    print(list[i])
    i=i+1