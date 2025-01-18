with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(text):
    counter = 0
    words =text.split()
    for word in words:
        counter +=1
    return counter

def count_characters(text):
    lowered_text = text.lower()
    from collections import Counter

    all_characters = Counter(lowered_text)
    all_characters_sorted = dict(sorted(all_characters.items(), key=lambda item: item[1], reverse=True))
    return all_characters_sorted

word_counter = count_words(file_contents)
character_counter = count_characters(file_contents)
letters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
filtered = {k: v for k, v in character_counter.items() if k in letters}

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_counter} words founf in the document")
print()
for key, count in filtered.items():
    print(f"The {key} character was found {count} times")
print("--- End report ---")