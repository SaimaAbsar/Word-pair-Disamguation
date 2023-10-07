# Evaluation
# Phase 5
import pandas as pd

def evaluate(predicted, pseudoword, output_dir):
    acc = 0
    # Read the ground truth file
    groundtruth = dict(pd.read_csv(output_dir+f"_{pseudoword}"+"_groundtruth.txt",\
        delimiter=": ", header=None, engine='python').to_dict(orient='split')['data'])
    for line in predicted:
        if predicted[line] == groundtruth[line]:    #compare predicted and ground truth for each line
            acc += 1
    N = len(predicted.keys())
    accuracy = acc/N *100   #determine percentage accuracy
    return(accuracy)
    


