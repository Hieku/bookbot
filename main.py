with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

def count_words (text):
    counter = 0
    words =text.split()
    for word in words:
        counter +=1
    return print(counter)

def count_characters(text):
    lowered_text = text.lower()
    
count_characters(file_contents)