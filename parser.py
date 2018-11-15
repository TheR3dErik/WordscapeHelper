fo = open("/Users/erik/Documents/python/wordscape_dict/words", "r")

words = fo.readlines()
fo.close()

output = open("/Users/erik/Documents/python/wordscape_dict/dictionary", "wb")

for word in words:
    if len(word) > 7 or len(word) < 4 or not word[0].islower():
        continue
       
    plural_word = word
    if (word[-2] == "f"):
        plural_word = word[:-2] + "ves\n"
    elif (word[-2] == "y"):
        plural_word = word[:-2] + "ies\n"
    else:
        plural_word = word[:-1] + "s\n"

    output.write(word)
    output.write(plural_word)
    if word == "boy\n":
        output.write("boys\n")

output.close()