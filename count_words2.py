import os.path

words_dict = {}

with open('word_text.txt',mode='r') as file:
    lines = file.readlines()
    print(lines)
    #line = file.read()
    for line in lines:
        words = line.lower().split()
        #print(words)
        for word in words:
            # count = words_dict.get(word)
            # if count is not None:
            #     count = count + 1
            #     words_dict[word] = count
            words_dict[word] = words_dict.get(word,0) + 1
            # else:
            #     words_dict[word] = 1


    print(words_dict)