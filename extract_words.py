def main():
    #opens the txt file and stores the text
    file = open("anthem.txt", 'r')

    allwords = file.read().rstrip().split()

    for word in allwords:
        word = word.lower()
