name = input('Enter your name: ')

if len(name) < 3:
    print(f"Your name has {len(name)} characters, Name must be 3 characters")
elif len(name) > 50:
    print(f"your name has {len(name)} characters, name can be a maximum of 50 characters")
else:
    print('Name looks good!')