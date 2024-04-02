import sys

def stdIn(userIn):                         
    phrase = userIn.lower()                                     # Read user input in lower case
    return phrase

def sentimentScore(stdIn):
    sentimentLexicon = {'confusing': '-2', 'congrats': '2',     # Assign lexicon score
         'happy': '5', 'sad': '-5'}
    
    s = list(stdIn.split(" "))                                  # Convert phrase string to list 
    
    score = 0   
    for x in s:                                                 # Iterate over phrase string
        for i in sentimentLexicon.keys():                       # Iterate lexicon dict keys for phrase match
            if x == i:
                score += int(sentimentLexicon[i])               # Increment score if match
    print('sentiment score: ' + str(score))

def main():
    userIn = sys.argv[1]
    phrase = stdIn(userIn)
    sentimentScore(phrase)

if __name__== '__main__':
     main()

