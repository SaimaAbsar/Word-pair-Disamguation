# SNLP Fall 22
# HW2 September 26, 2022
# Author: Saima Absar

import os
import argparse
import time
from Preprocess import preprocess
from Extracting_contexts import create_context
from Create_pseudowords import pseudo_replace
from Naive_bayes import compute_training_prob
from Disambiguate import disambiguate
from Evaluate import evaluate

# Get the start time
st = time.time()

# Function for the main process
def process(in_file, out_file):
    print("\nPreprocessing data...")
    data = preprocess(in_file) #returns a filtered string of words
    # Form a list of all the words in the questions
    all_senses = [["night", "seat"], ["kitchen", "cough"], ["car", "bike"], ["manufacturer", "bike"], ["big", "small"], ["huge", "heavy"]]
    Pseudo_list = ["nightseat", "kitchencough", "carbike", "manufacturerbike", "bigsmall", "hugeheavy"]
    window_size = 10 # window size to form context
    for i in range(len(all_senses)):
        sense_list = all_senses[i]
        pseudoword = Pseudo_list[i]
        print('\nWorking on: %s, that will be replaced with "%s"' %(sense_list,pseudoword))
        print("Extracting context with a window of %d..." %window_size)
        create_context(data,sense_list,window_size,out_file)
        print("Replacing the given word pairs with pseudowords...")
        train_dict, test_data, sense_freq = pseudo_replace(out_file, sense_list, pseudoword)
        print("Computing the probabilities from training corpus...")
        priors = compute_training_prob(train_dict, test_data, sense_list, sense_freq, out_file)
        print("Priors: ", priors)
        print("Using the training probabilites to disambiguate sense from test data..")
        predicted = disambiguate(test_data, priors, pseudoword, out_file)
        print("Evaluating the results...")
        accuracy = evaluate(predicted, pseudoword, out_file)
        print('Disambiguation accuracy: ', accuracy)


if __name__ == '__main__':  
    # User input for input and output directories
    parser = argparse.ArgumentParser("input directory")
    parser.add_argument("inpath", help="path to input directory", type=str)
    parser.add_argument("outpath", help="path to ouput directory", type=str)
    args = parser.parse_args()
    input_dir = args.inpath
    output_dir = args.outpath

    # Iterate through all files in the the input directory
    # read the text files and process it
    for file in os.listdir(input_dir):
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            in_file = f"{input_dir}/{file}"
            out_file = output_dir+'/'+file.replace('.txt','')  #name the output files names a/c to input files
            # process the specific file
            process(in_file, out_file)

# Get the end time
et = time.time()
# Get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')