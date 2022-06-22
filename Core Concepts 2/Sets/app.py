# list = []
# tuple = ()
# set = {}

lists = [1,2,3,4,5,6,5,4,4,1,6,2,8,7,7,'abc','abc']

no_duplicate_set = set(lists)
print(no_duplicate_set)

no_duplicate_set = list(no_duplicate_set)
print(no_duplicate_set)

lists = no_duplicate_set

print()

s = {'blueberry' , 'raspberry'}

s.add('Strawberry')
s.add('blueberry')

print(s)