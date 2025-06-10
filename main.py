import sys

from stats import get_char_count
from stats import get_word_count
from stats import sort_chars


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book = sys.argv[1]

    print(f"Analyzing book found at {book}...")
    text = get_book_text(book)

    print("----------- Word Count ----------")
    words = get_word_count(text)
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    chars = sort_chars(get_char_count(text))
    for c in chars:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")

    print("============= END ===============")

main()

