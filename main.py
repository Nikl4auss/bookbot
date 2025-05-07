import sys
from stats import (
    get_book_text,
    get_words_count,
    get_char_count,
    get_sorted_chart_count_list,
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found in {file_path}")
    print("----------- Word Count ----------")
    text = get_book_text(file_path)
    word_count = get_words_count(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = get_char_count(text)
    char_list = get_sorted_chart_count_list(char_count)

    for char in char_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")
    print("============= END ===============")


main()
