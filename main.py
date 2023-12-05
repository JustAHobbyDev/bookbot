

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count


def count_characters(text):
    character_counts = {}
    for character in text.lower():
        character_counts[character] = character_counts.get(character, 0) + 1
    return character_counts


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    character_count = count_characters(file_contents)

    print(f"--- Begin report of {f.name} ---")
    print(f"{word_count} words found in the document\n\n")

    characters = [ c for c in list(character_count) if c.isalpha() ]
    characters.sort(key=lambda character: character_count[character], reverse=True)

    for c in characters:
        print(f"The '{c}' character was found {character_count[c]} times")

    print("--- End report ---")

