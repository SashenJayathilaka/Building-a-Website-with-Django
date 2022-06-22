numbers = [5,2,7,5,9,5,4,10,18]
uniques = []

for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)