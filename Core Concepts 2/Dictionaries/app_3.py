from collections import OrderedDict

sentence1 = "Hello how are you Hello I'm fine how are you, I think you're ok what do you like to eat, I like to eat fruits"

world_counts = {
    'Hello': 1,
    'I': 1,
    'eat' : 3
}

world_counts['you'] = 4
world_counts['fine'] = 2

# dict.clear()
# world_counts.clear()

print(list(world_counts.values()))
print(sorted(list(world_counts.values())))