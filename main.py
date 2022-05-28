# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input("Please enter first word: ")
    anagram = input("Please enter second word: ")

    sort1 = sorted(word)
    sort2 = sorted(anagram)

    if (sort1 == sort2):
        print("True")
    else: 
        print("False")


find_anagram('word', 'anagram')