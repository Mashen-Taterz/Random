#Programming with Mosh
#https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=WL&index=52


#Small function for converting text into emojis

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "🙂",
        ":(": "🙁"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message)) 

