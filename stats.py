def get_words_count(text):
    words = text.split()
    return len(words)

def get_char_dict_usage(text):
    char_dict = {}
    for char in text:
        char_instance = char.lower()
        if char_instance not in char_dict:
            char_dict[char_instance] = 1
        else:
            char_dict[char_instance] += 1
    return char_dict
