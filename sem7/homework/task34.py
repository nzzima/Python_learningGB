def check_rhythm(poem):
    vowels = 'ауоыиэяюёе'
    if " " not in poem:
        print("Количество фраз должно быть больше одной!")
        return
    poem_words = poem.split(" ")
    print(poem_words)
    count_of_vowels = []
    for word in poem_words:
        count = 0
        for char in word:
            for vow in vowels:
                if char == vow:
                    count += 1
        count_of_vowels.append(count)
    print(count_of_vowels)
    if len(set(count_of_vowels)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")

input_poem = input("Enter poem: ")
check_rhythm(input_poem)
