import sys


def main():
    paths = get_paths()
    for path in paths:
        text = get_text(path)
        words_count = count_words(text)
        chars_dict = get_chars_dict(text)
        chars_dict_list = get_chars_dict_list(chars_dict)
        chars_dict_list.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of {path} ---")
        print(f"{words_count} words found in the document")
        for item in chars_dict_list:
            print(f"The '{item["name"]}' character was found {item["num"]} times")
        print("--- End report ---")


def get_paths():
    if len(sys.argv) < 2:
        print("No path provided, exiting...")
        sys.exit(1)
    return sys.argv[1:]


def get_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def get_chars_dict(text):
    chars_dict = {}
    for char in text:
        lowered = char.lower()
        if char not in chars_dict:
            chars_dict[lowered] = 1
        else:
            chars_dict[lowered] += 1
    return chars_dict


def get_chars_dict_list(chars_dict):
    chars_dict_list = []
    for key in chars_dict:
        chars_dict_list.append({"name": key, "num": chars_dict[key]})
    return chars_dict_list


def sort_on(dict):
    return dict["num"]


if __name__ == "__main__":
    main()
