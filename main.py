import sys

from stats import get_character_count, get_word_count, report


def get_book_text(path):
    with open(path) as f:
        contents = f.read()

    return contents


def main(path):
    content = get_book_text(path)

    # print("============ BOOKBOT ============")
    # print("Analyzing book found at books/frankenstein.txt...")
    # print("----------- Word Count ----------")
    words = get_word_count(content)
    print(words)
    # print("--------- Character Count -------")
    chars = get_character_count(content)
    for char in report(chars):
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    # print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    main(sys.argv[1])
