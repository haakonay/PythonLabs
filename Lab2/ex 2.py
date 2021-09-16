# read python file
# removing comma, full stop, new line etc
# dict with word + occurences pairs, and fill it with words of the text
# List all the words that are more than 3 times in the text

f = open("python.txt", "r")

for char in l

for line in f:
    for word in line.split():
        if word in ",.!?()''":
            word.replace(word, '')
            print(word)



f.close()
