def get_word_count(contents):
    words = contents.split()
    return f"Found {len(words)} total words"


def get_character_count(contents):
    chars = {}
    for c in contents:
        chars[c.lower()] = chars.get(c.lower(), 0) + 1

    return chars


def sort_on(dict):
    return dict["num"]


def report(characters):
    char_list = []
    for k, v in characters.items():
        entry = {"char": k, "num": v}
        char_list.append(entry)

    char_list.sort(reverse=True, key=sort_on)
    return char_list
