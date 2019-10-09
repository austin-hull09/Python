words = ['You', 'may', 'say', "I'm", 'a', 'dreamer']
words2 = []

def my_reverse(sentence, sentence2):
    for x in range(len(sentence)-1,-1,-1):
        sentence2.append(sentence[x])
    print(sentence2)
    
my_reverse(words, words2)
        
