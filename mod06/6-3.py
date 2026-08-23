t=bool(False)
while t==False:
    n=input("Syötä kokonaisluku: ")
    try:
        int(n)
    except:
        print("Luku ei kelpaa. Syötä vain numeroita.")
    else:
        n=int(n)
        t=True

comp=False
for i in range(n-1):
    if n/(i+1)==int(n/(i+1)):
        if i+1!=1:
            comp=True
            break
if comp==True:
    print(f'{n}{" ei ole alkuluku"}')
else:
    print(f'{n}{" on alkuluku"}')