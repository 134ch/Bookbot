def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_letters = get_count_letters(text)
    key_list = key_to_list(count_letters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"found {num_words} words on the documents")
    for key in key_list :
        print(f"the '{key}' characters was found {count_letters[key]} times")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f :
        text = f.read()"
    return text

def get_count_letters(text):
    lowtext = text.lower()
    count = {}
    for i in lowtext:
        if i not in count  :
            count[i] = 1
        else : count[i] += 1        
    return count

def key_to_list(object):
    list = []
    for key in object :
        if key.isalpha() :
            list.append(key)
        
    list.sort()

    return list
main()

