

def count_words(text_file):
    """Returns a count of how many times a word appears in the text file"""

    words_file = open(text_file)
    words_count = {}

    for line in words_file:
        line = line.split()
        for word in line:
            words_count[word] = words_count.get(word, 0) + 1

    words_file.close()
    return words_count


def prints_words_count(dict):
    """Prints dictionary created in count_words function"""

    for word, count in words_count.items():
        print(f"{word}: {count}")


words_count = count_words("twain.txt")
prints_words_count(words_count)
