names = ['Hasindu' , 'Tom' , 'Jane' , 'Oscar']

l = []
for person in names:
    l.append(person)
print(l)

print([person for person in names])

print()

l = []
for person in names:
    l.append(person + ' dumped me. ')
print(l)

print([person + ' dumped me. ' for person in names])

print()

movies_and_rating = {"Ticket to Paradise":9 , "The Fabelmans": 3 , "Halloween Ends": 3 , "Knock at the Cabin": 2 , "Untitled Tenth Chapter in Fast & Furious Saga": 8}

l = []
for movies in movies_and_rating:
    if movies_and_rating[movies] > 6:
        l.append(movies)
print(l)

print([movies for movies in movies_and_rating if movies_and_rating[movies] > 6])