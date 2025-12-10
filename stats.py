
def num_words(text):
    list = text.split()
    l = len(list)
    print(f"Found {l} total words")

def each_char(text):
    counts = {}
    for ch in text:
        low = ch.lower()
        if low in counts:
            counts[low] += 1
        else:
            counts[low] = 1
    return counts

def sort_on(item):
    return item["num"]

def dict_to_list(dict):
    list = []
    for d in dict:
        list.append({"char": d, "num": dict[d]})
    list.sort(reverse=True, key=sort_on)
    return list


