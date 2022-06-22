dictionary = {'bananas': 5, 'oranges': 3}

dictionary['bananas']
print(dictionary['bananas'])
print(dictionary['oranges'])

print()

contact = {
    'Joe' : {'phone' : "123-458" , 'email' : "Joe@gmail.com"},
    'Tom' : ["789-364" , "Tom@gmail.com"]
}

print(contact['Joe'])
print(contact['Tom'])

print()

sentence1 = "Marvel Comics is the brand name and primary imprint of Marvel Worldwide Inc., formerly Marvel Publishing, Inc. and Marvel Comics Group, a publisher of American comic books and related media. In 2009, The Walt Disney Company acquired Marvel Entertainment, Marvel Worldwide's parent company."
sentence1 = "Hello how are you Hello I'm fine how are you, I think you're ok what do you like to eat, I like to eat fruits"

world_counts = {
    'Hello': 1,
    'I': 2,
    'eat' : 3
}

# dict.items()
print(world_counts.items())

# dict.keys()
print(world_counts.keys())

# dict.values()
print(world_counts.values())

print()

print(world_counts)
world_counts.pop('I')
print(world_counts)

print()