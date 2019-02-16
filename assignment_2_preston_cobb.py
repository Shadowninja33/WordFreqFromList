def word_freq(names):
    """Takes in a list of strings and return a dictionary number of occurrences of each key"""
    namedict = dict()

    for word in names:
        if word not in namedict:
            namedict[word] = 1
        else:
            namedict[word] += 1

    return namedict


def asc_word_freq(dictionary):
    """Accepts dictionary and sorts in in ascending order by values"""
    ascdict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
    return ascdict


def desc_word_freq(dictionary):
    """Accepts dictionary and sorts in in descending order by values"""
    descdict = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    return descdict


def size_dict(dictionary, size):
    """Takes a dictionary and a size int, and returns size number of key value pairs, from greatest to smallest"""
    sizedict = dict()
    if size <= 0:
        return sizedict

    if size >= len(dictionary):
        return dictionary

    sort = dict(list(desc_word_freq(dictionary).items())[:size])
    return sort


if __name__ == "__main__":
    names = ["Liam", "Mason", "William", "Noah", "William", "James", "Sophia", "Logan",
             "Benjamin", "Mason", "Elijah", "Oliver", "Jacob", "Emma", "Olivia", "Ava",
             "William", "Isabella", "Oliver", "Sophia", "Mia", "Charlotte", "Amelia",
             "William", "Evelyn", "Abigail", "Olivia", "Ava", "Mason", "Isabella", "Noah",
             "William", "James", "Olivia", "Amelia", "Oliver", "William"]

