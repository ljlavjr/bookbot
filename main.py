import sys
from stats import num_words, each_char, dict_to_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(f"./{sys.argv[1]}")
    dict = each_char(text)
    list = dict_to_list(dict)
    print("============ BOOTBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("------------ Word Count ------------")
    num_words(text)
    print("--------- Character Count ----------")
    for i in list:
        ch = i["char"]
        num = i["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")

main()



