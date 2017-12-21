#!/usr/bin/env python3

word = input("Please enter a word to translate: ")

for d in open('dictionary.txt', 'r').readlines():
    word_ucase = word.upper()
    if d.upper().startswith(f"{word_ucase}"):
        english = d.split(':')[0]
        translated = d.split(':')[1].strip()
        print(f"{english} is {translated} in German")

