def get_book_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count


def character_counter(book_text):
    chars_count = {}
    words = book_text.split()

    for word in words:
        for char in word.lower():
            if char not in chars_count:
                chars_count[char] = 1
            else:
                chars_count[char] += 1
    
    return chars_count


def sort_chars(characters):
    # print(characters)
    char_list = []
    for char in characters:
        char_list.append({
            "char": char,
            "num": characters[char]
        })
    
    char_list.sort(reverse=True, key=sort_helper)
    return char_list


def sort_helper(char_list):
    return char_list["num"]