#from collections import defaultdict

def main():
    #opens the txt file and stores the text
    #file = open("anthem.txt", 'r')

    #allwords = file.read().rstrip().split()
    allwords = ["apple", "apple", "orange", "yes", "yes", "yes", "no"]
    for word in allwords:
        word = word.lower()

    #word freq
    word_freq = {}
    for word in allwords:
        if (word in word_freq):
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    #sorts by increasing freq
    word_freq = sorted(((y,x) for x,y in word_freq.items()))
    
    print(word_freq)
    #writes to wordfrequency file
    word_frequency = open("wordfrequency.txt", 'w')
    for word in word_freq:
        line = str(word) + ": "
        print(word_freq[word])
        word_frequency.write(line)
        
    #unique words
    unique_words = open("uniquewords.txt", 'w')
    
    for word in word_freq:
        if (word_freq[word] == 1):
            line = str(word) + "\n"
            unique_words.write(line)
    print(unique_words)
    print("done")
    #file.close()
    
main()
