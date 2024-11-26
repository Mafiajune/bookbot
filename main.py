def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("===Begin of report of frankenstein.txt===")
    print(f"{num_words} words have been found in the document")
    chars_dict = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print()
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("=====End Report=====")
        



def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    count = {}
    for letter in text:
        lowerd = letter.lower()
        if lowerd in count:
            count[lowerd] += 1
        else: 
            count[lowerd] = 1 
    return count
 
def sort_on(dict):
    return dict["num"]
    
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char":ch,"num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()