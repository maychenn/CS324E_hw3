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

    #frequency of each word
    word_freq = dict()
    for word in allwords:
        if (word in word_freq):
            word_freq[word] += 1
        else:
            word_freq[word] = 1
            
    #frequency of word frequency
    freq_word_freq = dict()
    for word in word_freq:
        if word_freq[word] in freq_word_freq:
            freq_word_freq[word_freq[word]] += 1
        else:
            freq_word_freq[word_freq[word]] = 1
            
    #sorts by increasing word frequency (freq_word_freq is now a 2D list)
    word_freq = sorted(([y,x] for x,y in word_freq.items()))
    
    #sorts by increasing freq of word freq (freq_word_freq is now a 2D list)
    freq_word_freq = sorted(([x,y] for x,y in freq_word_freq.items()))
    
    #writes to wordfrequency file
    word_frequency = open("wordfrequency.txt", 'w')
    counter = 0
    for freq in freq_word_freq:
        if counter < len(freq_word_freq)-1:
            line = str(freq[0]) + ": " + str(freq[1]) + "\n"
            counter += 1
        else:
            line = str(freq[0]) + ": " + str(freq[1])
        word_frequency.write(line)
        
    #unique words
    unique_words = open("uniquewords.txt", 'w')

    for word in range(len(word_freq)):
        if (word_freq[word][0] == 1) and (word_freq[word+1][0] == 1):
            line = str(word_freq[word][1]) + "\n"
            unique_words.write(line)
        else:
            line = str(word_freq[word][1])
            unique_words.write(line)
            break

    file.close()
    unique_words.close()
    word_frequency.close()
    
main()
