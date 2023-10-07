# Naive Bayes implementation from scratch for text classification
# Phase 3
# Training from the training corpus

from collections import Counter

# Get the V frequency
def compute_V(train_dict):
    mystr = ''
    for x in train_dict.values():
        for y in x:
            mystr += ' ' + y
    V_freq = Counter(mystr.split())
    return(V_freq)

# Get count(w,c) and count(c) for each sense
# count_w_c = number of times w occurred in training set for c
# count_c = number of tokens in training set for c 
def word_counter(train_dict, sense):
    count_w_c = Counter(" ".join(train_dict[sense]).split()) 
    count_c = len(count_w_c.keys()) 
    return(count_w_c,count_c)

# Determine P(w|c) for each word in trainin_corpus
def word_likelihood(w, count_w_c, count_c, V, V_freq):
    if w in V_freq.keys(): freq_w = count_w_c[w]
    else: freq_w = 0
    prob_w = (freq_w+1) / (count_c+V)
    return(prob_w)
    

# Compute Prior probabilities of each prior
def compute_prior(sense_list, sense_freq):
    priors = {}
    N = sum(sense_freq.values())
    for sense in sense_list:
        priors[sense] = sense_freq[sense]/N #the number of instances of that class/total instances
    return priors

# Train
def compute_training_prob(train_dict, test_data, sense_list, sense_freq, output_dir):
    # Get the prior probabilities
    priors = compute_prior(sense_list, sense_freq)
    V_freq = compute_V(train_dict)
    # Get the V
    V = len(V_freq.keys())   
    word_prob = {}
    for sense in sense_list:
        count_w_c, count_c = word_counter(train_dict, sense)
        test_words = " ".join(test_data).split()
        for w in test_words:
            word_prob[w] = word_likelihood(w, count_w_c, count_c, V, V_freq)
        # Save the trained prob for each word in traing corpus
        path = output_dir+f"_{sense}"+"_Wprob.txt"
        with open(path, 'w') as f:
            for word in word_prob:
                f.write("%s: %s\n" %(str(word), float(word_prob[word])))
    return(priors)

            
        