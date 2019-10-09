# Austin Hull

# Question 1
import statistics
l1 = [1,3]
print(statistics.median(l1))
print(statistics.median_low(l1))


#Question 2

words = ['You', 'may', 'say', "I'm", 'a', 'dreamer']

def count_characters(sentence):
    total = 0
    for word in sentence:
        total += len(word)
    print(total)
    
count_characters(words)


#Question 3

words = ['You', 'may', 'say', "I'm", 'a', 'dreamer']
words2 = []

def my_reverse(sentence, sentence2):
    for x in range(len(sentence)-1,-1,-1):
        sentence2.append(sentence[x])
    print(sentence2)
    
my_reverse(words, words2)
        

#Question 4

def create_file(file_name, n):
    x = 0
    for i in range(n):
        x += 1
        file_name.write(str(x))
        file_name.write("\n")

output = open("file.out", "w")

create_file(output, 1000)

output.close()
