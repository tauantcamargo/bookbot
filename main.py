from sys import argv

from stats import get_char_dict_usage, get_words_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_book_text_presentation(filepath):
    print(f"Analyzing book found at {filepath}...")
    text_present_in_book = get_book_text(f"./{filepath}")
    print("----------- Word Count ----------")
    print(f"Found {get_words_count(text_present_in_book)} total words")
    return text_present_in_book

def get_char_usage_presentation(usage_dict):
    print("--------- Character Count -------")
    for char in usage_dict:
        print(f"{char}: {usage_dict[char]}")


def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    print("============ BOOKBOT ============")
    text_in_book = get_book_text_presentation(argv[1])
    char_usage = get_char_dict_usage(text_in_book)
    get_char_usage_presentation(char_usage)
    print("============= END ===============")


main()
