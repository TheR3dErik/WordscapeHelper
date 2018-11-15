fo = open("words", "r")

words = fo.readlines()
fo.close()

words_to_output = []

for word in words:
    if not word[:-1].isalpha() or len(word) > 7 or len(word) < 4 or not word[0].islower():
        continue

    plural_word = word
    if (word[-2] == "f"):
        plural_word = word[:-2] + "ves\n"
    elif (word[-2:] == "oy" or word[-2:] == "ay" or word[-2:] == "ey"):
        plural_word = word[:-1] + "s\n"
    elif (word[-2] == "y"):
        plural_word = word[:-2] + "ies\n"
    elif (word[-2] == "s"):
        plural_word = word[:-1] + "es\n"
    elif (word[-2] == "x"):
        plural_word = word[:-1] + "es\n"
    else:
        plural_word = word[:-1] + "s\n"

    words_to_output.append(word)
    words_to_output.append(plural_word)

words_to_output = list(set(words_to_output))

output = open("dictionary", "w")

for word in words_to_output:
    output.write(word)

output.close()
