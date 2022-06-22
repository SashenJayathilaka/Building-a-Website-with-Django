sentence1 = "Hello how are you Hello I'm fine how are you, I think you're ok what do you like to eat, I like to eat fruits"

world_counts = {
    'Hello': 1,
    'I': 1,
    'eat' : 3
}

print(world_counts)
world_counts['like'] = 2
print(world_counts)

print()

# dict.popitem()
print(world_counts)
print(world_counts.popitem())
print(world_counts)