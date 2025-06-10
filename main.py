from stats import get_char_count
from stats import get_word_count
from stats import sort_chars


BOOKS_PATH = "./books/{}.txt"


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")

    book = "frankenstein"
    text = get_book_text(BOOKS_PATH.format(book))
    print(f"Analyzing book found at {BOOKS_PATH.format(book)}...")

    words = get_word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    chars = sort_chars(get_char_count(text))
    print("--------- Character Count -------")
    for c in chars:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")

    print("============= END ===============")

main()

