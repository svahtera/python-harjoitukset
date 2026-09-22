def oddsRemover(list):
    evens=[]
    for i in list:
        if i % 2 == 0:
            evens.append(i)
    return evens

num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
new=oddsRemover(num)
print(num)
print(new)