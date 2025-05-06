import sys
import logging
from stats import count_words, count_chars, get_chars_dict_list


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    paths = get_paths()
    for path in paths:
        text = get_text(path)
        if text is None:
            continue
        if not text.strip():
            print(f"--- Begin report of {path} ---")
            print("The file is empty or contains no readable text.")
            print("--- End report ---\n")
            continue
        words_count = count_words(text)
        chars_dict = count_chars(text)
        chars_dict_list = get_chars_dict_list(chars_dict)
        chars_dict_list.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of {path} ---")
        print(f"Found {words_count} total words")
        for item in chars_dict_list:
            print(f"{item['char']}: {item['num']}")
        print("--- End report ---")


def get_paths():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1:]

def get_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        logging.error(f"The file '{path}' does not exist.")
    except PermissionError:
        logging.error(f"Permission denied for '{path}'.")
    except Exception as e:
        logging.error(f"An unexpected error occurred while reading '{path}': {e}")
    return None



def sort_on(dict):
    return dict["num"]


if __name__ == "__main__":
    main()
