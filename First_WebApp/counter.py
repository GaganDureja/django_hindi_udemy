import operator


def count(text):
    words = text.split()
    word_count = len(words)
    dict_words = {}
    for word in words:
        if (word in dict_words):
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    sort_dict = sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)
    return sort_dict,word_count