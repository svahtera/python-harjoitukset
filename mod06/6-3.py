n=int(input("Syötä kokonaisluku: "))

comp=False
for i in range(0, n-1):
    if n/(i+1)==int(n/(i+1)):
        if i+1!=1:
            comp=True
            break
if comp==True:
    print(f'{n}{" ei ole alkuluku"}')
else:
    print(f'{n}{" on alkuluku"}')