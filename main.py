from NGrams import find_bigrams, find_ngrams


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1 = find_bigrams("poop")
    list2 = []
    for p in list1:
        print(p)
        b = ("").join(p)
        print(b)
        list2.append(b)

    print(list2)




