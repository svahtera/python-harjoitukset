def adup(r):
    total=0
    for i in range(r):
        total=total+int(numbers[i])
    return total

numbers=[1,2,3,4,5]
print(adup(len(numbers)))