def main(file_path):
    print(f"--- Begin report for {file_path} ---")
    with open(file_path) as file_object:
        file_contents = file_object.read()
        return file_contents

def count_words():
    book_content = main('books/frankenstein.txt')
    words = len(book_content.split())
    print(words, 'words found in the document')

def count_caracters():
    my_string = main('books/frankenstein.txt')
    lowered_string = my_string.lower()
    characters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    for word in lowered_string:
          if word in characters:
              characters[word] +=1

    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)

    for word, count in sorted_characters:
        print(f'The character "{word}" was found {count} times')  

count_words()
print()
count_caracters()
