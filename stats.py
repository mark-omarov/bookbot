def count_words(text):
    return len(text.split())


def count_chars(text):
    chars_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered == "":
            continue
        if lowered not in chars_dict:
            chars_dict[lowered] = 1
        else:
            chars_dict[lowered] += 1
    return chars_dict

def get_chars_dict_list(chars_dict):
    return [{"char": key, "num": chars_dict[key]} for key in chars_dict]