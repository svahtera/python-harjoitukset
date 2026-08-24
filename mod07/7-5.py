def oddsRemover():
    justEvens=[]
    r=len(num)
    for i in range(r):
        if int(num[i]/2)!=num[i]/2:
            justEvens.append(i)
    return justEvens

num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
new=oddsRemover()
print(num)
print(new)