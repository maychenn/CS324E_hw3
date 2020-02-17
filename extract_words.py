#from collections import defaultdict
import re #regular expression

def main():
    #opens the txt file and stores the text
    file = open("anthem.txt", 'r')
    
    #allwords
    #opens an alternate txt file and stores the text
    file_alt = open("anthem.txt", "r", encoding = "utf-8")
    
    #stores text as a string with all lowercase characters 
    allwords = file_alt.read().lower()
    
    #split string into list with non-alphabetical characters (or groups of characters) as delimiters
    allwords = re.findall(r"[a-z]+", allwords)
    
    #append linebreak to all but last word
    allwords_linebreaks = allwords.copy()
    for word_index in range(len(allwords_linebreaks)-1):
        allwords_linebreaks[word_index] = allwords_linebreaks[word_index]+"\n"
        
    #creates txt file for allwords output
    allwords_outfile = open("allwords.txt", "w")
    allwords_outfile.writelines(allwords_linebreaks)
    file_alt.close()
    allwords_outfile.close()

    
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
