paragraph = input("Enter a paragraph: ")

# Convert to lowercase and remove punctuation marks.
clean_text = ""
for character in paragraph.lower():
    if character.isalnum() or character.isspace():
        clean_text += character

words = clean_text.split()

if len(words) == 0:
    print("Please enter some text.")
else:
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("\nWord frequency:")
    print(frequency)

    n = int(input("\nHow many top words should be displayed? "))
    sorted_words = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))

    print("\nTop words:")
    for word, count in sorted_words[:max(0, n)]:
        print(word, ":", count)

    single_words = []
    for word, count in frequency.items():
        if count == 1:
            single_words.append(word)
    print("\nWords used only once:", sorted(single_words))

    reverse_frequency = {}
    for word, count in frequency.items():
        if count not in reverse_frequency:
            reverse_frequency[count] = []
        reverse_frequency[count].append(word)

    for count in reverse_frequency:
        reverse_frequency[count].sort()
    print("\nFrequency-wise words:", reverse_frequency)

    length_groups = {}
    for word in frequency:
        size = len(word)
        if size not in length_groups:
            length_groups[size] = []
        length_groups[size].append(word)

    for size in length_groups:
        length_groups[size].sort()
    print("\nWords grouped by length:", length_groups)

    search_word = input("\nEnter a word to search: ").lower()
    search_word = "".join(ch for ch in search_word if ch.isalnum())

    if search_word in frequency:
        print(search_word, "appears", frequency[search_word], "time(s).")
    else:
        print("Word not found.")
