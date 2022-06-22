digits = [0,1,2,3,4,5,6,7,8,9]
name = "First Last"

print(digits)

print(digits[-1])
print(digits[-2])
print(digits[-3])
print(digits[-4])

print()

print(digits[1:5])
print(name[0:6])

print(digits[5:10])

print(digits[0:10:3])  # x

print()

print(digits[::-1])
print(digits[::-3])

print(digits[5:0:-2])
print(digits[8:1:-3])

print()
print()

for i in range(len(digits)):
    print(digits[0:i])

print()

for i in range(len(digits)):
    print(digits[i:i+3])

print()

window_size = 5
for i in range(len(digits)-5):
    print(digits[i:i+window_size])

print()

window_size = 7
for i in range(len(digits)-window_size + 1):
    print(digits[i:i+window_size])


print()

window_size = 1
for i in range(len(digits)-window_size + 1):
    print(digits[i:i+window_size])