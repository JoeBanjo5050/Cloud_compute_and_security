import sys

def readFile(filename):                              # Read file passed to script and return contents
    contents = open(filename).read().lower().split()
    return contents 

def wordCount(contents):
    unique = []                                      # Set of unique words.
    for word in contents:
        if word not in unique:
            unique.append(word)
    
    # List of Stop words to exclude from the count
    stopWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", 
        "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", 
        "himself", "she", "her", "hers", "herself", "it", "its", "itself", 
        "they", "them", "their", "theirs", "themselves", "what", "which", 
        "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
        "was", "were", "be", "been", "being", "have", "has", "had", "having", 
        "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", 
        "or", "because", "as", "until", "while", "of", "at", "by", "for", 
        "with", "about", "against", "between", "into", "through", "during", 
        "before", "after", "above", "below", "to", "from", "up", "down", "in", 
        "out", "on", "off", "over", "under", "again", "further", "then", "once", 
        "here", "there", "when", "where", "why", "how", "all", "any", "both", 
        "each", "few", "more", "most", "other", "some", "such", "no", "nor", 
        "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", 
        "can", "will", "just", "don", "should", "now"]

    counts = []                                      # Set of unique word counts.
    for uniWord in unique:
        count = 0                                   
        for word in contents:                        # Iterate over contents.
            if word not in stopWords:                # Check for stop words
                if word == uniWord:                  # Test if word equal to the current unique word
                    count += 1                       # Increment count  
        counts.append(count)

    wordCountDict = {}                               # Create Dict of counts / unique to sort
    for key, val in zip(unique, counts):            
        wordCountDict.setdefault(key, []).append(val)
    return wordCountDict

def topTenWords(wordCountDict):                         
    wordCountDict_Sorted = sorted(wordCountDict,   
            key=wordCountDict.get, reverse=True)     #Sort by dict key, descending
    for i in wordCountDict_Sorted[:10]:              # Print top 10
        print(i, wordCountDict[i])

def main():
    filename = sys.argv[1]
    contents = readFile(filename)
    wordCountDict = wordCount(contents)
    topTenWords(wordCountDict)

if __name__== '__main__':
     main()
