list1 = [1,2,3,4,5,6]
list2 = ['one', 'two' , 'three' , 'four' , 'five' , 'six']

zipped = list(zip(list1 , list2))
print(zipped)

unZipped = list(zip(*zipped))
print(unZipped)

# for l1 , l2 in zip(list1 , list2):
    # print(l1)
    # print(l2)

print()

items = ['Apple' , 'Banana' , 'Orange']
counts = [3 , 4 , 5]
price = [0.99 , 0.25 , 0.50]

sentences = []
for (item , count ,price) in zip(items , counts , price):
    item , count ,price = str(item) , str(count) , str(price)
    sentence = 'I bought ' + count + ' ' + item + ' s at ' + price + ' cents each.'
    sentences.append(sentence)
print(sentences)