from stats import get_num_words, get_map_num_words, sort_char_map
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    book_title = sys.argv[1]
    content = get_book_text(f'./{book_title}')

    print(f"Analyzing book found at books/{book_title}")

    num_of_words = get_num_words(content)
    word_map = get_map_num_words(content)

    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")

    print("--------- Character Count -------")
    double_kv_map = sort_char_map(word_map)
    for val in double_kv_map:
        if val["char"].isalpha():
            print(f"{val["char"]}: {val["nums"]}")

main()
