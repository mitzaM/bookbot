def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for l in text:
        c = l.lower()
        if c not in char_dict:
            char_dict[c] = 0
        char_dict[c] += 1
    return char_dict

def sort_chars(chars_dict):
    l = [{"char": c, "num": n} for c, n in chars_dict.items()]
    l.sort(key=lambda x: x['num'], reverse=True)
    return l

