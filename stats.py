def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def get_words_count(text):
    return len(text.split())


def get_char_count(text):
    characters = list(text)
    char_count = {}

    for char in characters:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count


def get_sorted_chart_count_list(char_count):
    char_count_list = []
    for char, count in char_count.items():
        char_count_list.append({"char": char, "count": count})
    return sorted(char_count_list, key=lambda x: x["count"], reverse=True)
