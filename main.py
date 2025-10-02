import sys
from stats import get_book_word_count
from stats import character_counter
from stats import sort_chars


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    num_words = get_book_word_count(book_text)
    character_counts = character_counter(book_text)
    sorted_char_by_counts = sort_chars(character_counts)

    # print(f"{sort_chars(character_counts)}")
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    
    for char_dict in sorted_char_by_counts:
        if not char_dict["char"].isalpha():
            continue
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    
    print("============= END ===============")

main()