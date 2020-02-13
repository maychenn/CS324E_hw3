#from collections import defaultdict

def main():
    #opens the txt file and stores the text
    file = open("anthem.txt", 'r')
    
    ###insert code for allwords here

    #allwords = ["apple", "apple", "orange", "yes", "yes", "yes", "no"]
    for word in allwords:
        word = word.lower()

    #word freq
    word_freq = dict()
    for word in allwords:
        if (word in word_freq):
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    print(word_freq)
    
    #sorts by increasing freq (word_freq is now a list of lists)
    word_freq = sorted(([y,x] for x,y in word_freq.items()))
    print(word_freq)
    
    #writes to wordfrequency file
    word_frequency = open("wordfrequency.txt", 'w')
    for freq in word_freq:
        line = str(freq[0]) + ": " + freq[1] + "\n"
        word_frequency.write(line)
        
    #unique words
    unique_words = open("uniquewords.txt", 'w')
    
    for word in word_freq:
        if (word[0] == 1):
            line = str(word[1]) + "\n"
            unique_words.write(line)

    print("done")

    #file.close()
    
main()
