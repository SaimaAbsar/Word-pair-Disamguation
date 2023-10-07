# Extracting Contexts
# Phase 1

from doctest import testfile
import math

# Locate and generate a window of +/- 10 words around each sense
def extract_context(filtered_sentences, sense, window):
    context = []
    for sentence in filtered_sentences:       
        for word in sentence:
            feature = []
            if word == sense: 
                index = sentence.index(sense)
                if index-window>0:                              # check if there 10 words before the key word
                    feature.extend(sentence[index-10:index])    # add the words as feature
                else: feature.extend(sentence[:index])          # if not enough words in the sentence, add all the words there are
                if index+window<len(sentence):                  # check if there 10 words after the key word
                    feature.extend(sentence[index:index+10])    # form feature just as above
                else: feature.extend(sentence[index:])
                context.append(feature)
    return(context)

def create_context(filtered_sentences,sense_list, window, output_dir):
    train_data = {}
    test_data = {}
    for sense in sense_list:
        context = extract_context(filtered_sentences, sense, window)
        n = len(context)                                        # determine how many sentences extract as context
        train_data[sense] = context[0:math.ceil(0.8*n)]                # assign 80% of context to training data
        test_data[sense] = context[math.ceil(0.8*n):]                  # the rest to test data 
        print('size of train: ', len(train_data[sense]))     
        print('size of test: ', len(test_data[sense]))         
    train_length = min(len(i) for i in train_data.values())
    test_length = min(len(i) for i in test_data.values())
    print(train_length, test_length)
    for sense in sense_list:    
        train_path = output_dir+f"_{sense}"+"_train.txt"
        test_path = output_dir+f"_{sense}"+"_test.txt"
        with open(train_path, 'w') as out:
            for line in train_data[sense][0:train_length]:
                for w in line:
                    out.write("%s " %w)                         # save the train data into a text
                out.write("\n")
        with open(test_path, 'w') as out:                       # save the test data into a text
            for line in test_data[sense][0:test_length]:
                for w in line:
                    out.write("%s " %w)
                out.write("\n")

