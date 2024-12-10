import argparse


def main():
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
        chars_dict = get_chars_dict(text)
        chars_dict_list = get_chars_dict_list(chars_dict)
        chars_dict_list.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of {path} ---")
        print(f"{words_count} words found in the document")
        for item in chars_dict_list:
            print(f"The '{item['name']}' character was found {item['num']} times")
        print("--- End report ---")


def get_paths():
    parser = argparse.ArgumentParser(
        description="Generate a character frequency report for one or more text files."
    )
    parser.add_argument("paths", nargs="+", help="One or more paths to text files.")
    args = parser.parse_args()
    return args.paths


def get_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading '{path}': {e}")
    return None


def count_words(text):
    return len(text.split())


def get_chars_dict(text):
    chars_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered.strip() == "":
            continue
        if char not in chars_dict:
            chars_dict[lowered] = 1
        else:
            chars_dict[lowered] += 1
    return chars_dict


def get_chars_dict_list(chars_dict):
    return [{"name": key, "num": chars_dict[key]} for key in chars_dict]


def sort_on(dict):
    return dict["num"]


if __name__ == "__main__":
    main()
