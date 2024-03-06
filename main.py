def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        content = f.read()
        print(f"--- Begin report of {file} ---")
        wc = get_word_count(content)
        print(f"{wc} words found in the document\n")
        charDict = get_letter_count(content)
        charList = []
        for char in charDict:
            charList.append({"letter": char, "count": charDict[char]})
        charList.sort(reverse=True, key=sort_on)
        for char in charList:
            print(f"The '{char["letter"]}' character was found {char["count"]} times")
        print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letters = {}
    for char in text:
        if (not char.isalpha()):
            continue
        lower = char.lower()
        if (lower in letters):
            letters[lower] += 1
        else:
            letters[lower] = 1
    return letters

main()