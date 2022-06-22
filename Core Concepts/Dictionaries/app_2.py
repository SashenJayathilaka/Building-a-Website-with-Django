phone = input("Phone: ")

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
outPut = " "
for i in phone:
    outPut += numbers.get(i, "!") + " "
print(outPut)