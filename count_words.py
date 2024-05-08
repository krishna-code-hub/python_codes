

words_dict = {}

with open('word_text.txt',mode='r') as file:
    full_content = file.read()
    print(full_content)
    words = full_content.split()
    for word in words:
        count = words_dict.get(word)
        if count is not None:
            count = count + 1
            words_dict[word] = count
        else:
            words_dict[word] = 1

    print(words_dict)