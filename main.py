import sys
from stats import get_word_count, get_char_frequency, get_sorted_dicts

# Function to read a file from provided path and write its content to a string
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

# Function to get the value of the 'char' key in dictionary
def get_char(c):
    return c["char"]

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with error code if incorrect number of arguments provided

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_word_count(text)
    num_each_char = get_char_frequency(text)
    num_char_sorted = get_sorted_dicts(num_each_char)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for c in num_char_sorted:
        if get_char(c).isalpha() == False:
            continue
        print(f'{c["char"]}: {c["num"]}')

# Call main function to execute program
main()