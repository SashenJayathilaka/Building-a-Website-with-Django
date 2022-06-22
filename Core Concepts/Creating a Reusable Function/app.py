def emoji_convener(message):
    words = message.split(' ')

    emojis = {

        ":)": "😀",
        "(:": "😥"
    }

    output = ""
    for i in words:
        # print(i)
        output += emojis.get(i , i) + " "
    return output


message = input("> ")
print(emoji_convener(message))