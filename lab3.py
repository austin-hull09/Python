# --------------------------------------
# CSCI 127, Lab 3
# September 19, 2017
# Austin Hull
# --------------------------------------

def count_vowels(sentence):
    a = sentence.count('a')
    e = sentence.count('e')
    i = sentence.count('i')
    o = sentence.count('o')
    u = sentence.count('u')
    return a + e + i + o + u

def count_vowels_iterative(sentence):
    count = 0
    for vowel in (sentence):
        if (vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u'):
            count = count + 1
    return count

def count_vowels_recursive(sentence):
    if sentence == "":
        return 0
    elif sentence[0] == 'a' or sentence[0] == 'e' or sentence[0] == 'i' or sentence[0] == 'o' or sentence[0] == 'u':
        return 1 + count_vowels_recursive(sentence[1:])
    else:
        return 0 + count_vowels_recursive(sentence[1:])
# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence to evaluate: ")
        sentence = sentence.lower()     # convert to lowercase
        print()
        print("Number of vowels using count     =", count_vowels(sentence))
        print("Number of vowels using iteration =", count_vowels_iterative(sentence))
        print("Number of vowels using recursion =", count_vowels_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
