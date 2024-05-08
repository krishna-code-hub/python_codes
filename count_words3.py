

words_dict = {}

with open('word_text.txt',mode='r') as file:
    lines = file.readlines()
    for line in lines:
        words = line.lower().split()
        for word in words:
            words_dict[word] = words_dict.get(word,0) + 1

    print(words_dict)