def find_bigrams(word):
    input_list = list(word)
    return list(zip(input_list, input_list[1:]))


def find_ngrams(s, n):
    input_list = list(s)
    return list(zip(*[input_list[i:] for i in range(n)]))