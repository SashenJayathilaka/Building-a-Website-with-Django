problems = 'broke , pale , short , nerdy'
print(problems)

l = problems.split("short")

print(l)

print()

problems = 'broke , pale , short , nerdy'

l = problems.split(", ")

print(l)

joined = ' and '.join(l)
print(joined)

csv = 'or '.join(l)
print(csv)