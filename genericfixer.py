import sys

print(sys.argv[1:])
file_to_open = sys.argv[1]
word_to_change = sys.argv[2]
new_word = sys.argv[3]

with open(file_to_open, "r") as f:
    text = f.read()
    text = text.replace(word_to_change, new_word)
    with open("fixed_"+file_to_open, "w") as new_f:
        new_f.write(text)

print("We Done")
