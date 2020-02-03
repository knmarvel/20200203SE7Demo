#!/user/bin/env python
with open("fix_me.txt") as f:
    # context manager: we're opening a file, we're calling that import f,
    # you have stay in this code block to keep using "f". could also say
    # open "rhyme.txt"
    text = f.read()
    text = text.replace("cliant", "client")
    with open("fixed_rhyme.txt", "w") as new_f:
        new_f.write(text)
print("We Done")
