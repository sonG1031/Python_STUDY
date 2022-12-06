with open('words.txt', 'r') as file:
    words = file.read().split('\n')
    for word in words:
        if word == word[::-1]:
            print(word)