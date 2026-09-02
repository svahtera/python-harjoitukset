def oddsRemover():
    evens=[]
    r=len(num)
    for i in range(0, r, 2):
        evens.append(i)
    return evens

num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
new=oddsRemover()
print(num)
print(new)