import string

def ispangram(sentence):
    """
    Check whether a sentence is a pangram.

    """

    # 1. Normalize the sentence
    sentence = sentence.lower().replace(" ", "")

    # 2. Convert sentence to a set of characters
    letters_in_sentence = set(sentence)

    # 3. Create a set of all lowercase alphabet letters
    alphabet = set(string.ascii_lowercase)

    # 4. Find which letters are missing
    missing_letters = alphabet - letters_in_sentence

    # 5. Determine if pangram
    is_pangram = len(missing_letters) == 0

    return is_pangram, sorted(missing_letters)



# we gonna read from txt file

file_path = "sentence.txt"

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        sentence = line.strip()
        is_pangram, missing = ispangram(sentence)

        if is_pangram:
            print(f'"{sentence}" -> Pangram')
        else:
            print(f'"{sentence}" -> NOT pangram')
            print("   Missing letters:", ", ".join(missing))
