words = ['You', 'may', 'say', "I'm", 'a', 'dreamer']

def count_characters(sentence):
    total = 0
    for word in sentence:
        total += len(word)
    print(total)
    
count_characters(words)


        
