# Preprocessing Data

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re
from nltk import tokenize

# Remove stopwords
def remove_stopwords(words):
    # collect the set of stopwords from the nltk english database
    stopset = set(stopwords.words('english'))
    filtered = []
    for w in words:
        # remove the stopwords
        if not w in stopset:
            filtered.append(w) 
    #return(filtered)
    return(filtered)

# My own generation of tokens
def generate_tokens(content):
    # collected tokens only contain letters a-z upper OR lower
    match_pattern = re.findall(r'\b[a-zA-Z]{3,15}\b', content)
    words = []
    for word in match_pattern:
        words.append(str(word))
    words = [w.lower() for w in words]
    return words

# main function
def preprocess(path):  
    file = open(path) #Loading the data
    content = file.read() #converts into string
    sentences = tokenize.sent_tokenize(content) # collect the sentences
    file.close()
    filtered_sentences = []
    for s in sentences:
        tokens = generate_tokens(s)
        #print('My generated tokens: ', tokens)
        filtered = remove_stopwords(tokens)
        #print('filtered: ', filtered)
        filtered_sentences.append(filtered)
    #tokens = generate_tokens(content) #return the tokens
    #filtered = remove_stopwords(tokens) #remove stopwords
    return(filtered_sentences)
