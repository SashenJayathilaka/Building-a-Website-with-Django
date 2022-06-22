message = input("> ")
words = message.split(' ')

emojis = {

    ":)": "😀",
    "(:": "😥"
}

output = ""
for i in words:
    # print(i)
    output += emojis.get(i , i) + " "
print(output)