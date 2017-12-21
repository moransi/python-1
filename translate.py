
word = input("Please enter a word to translate: ")

for d in open('dictionary.txt', 'r').readlines():
    if d.startswith(f"{word}"):
        english = d.split(':')[0]
        translated = d.split(':')[1].strip()
        print(f"{english} is {translated} in German")

