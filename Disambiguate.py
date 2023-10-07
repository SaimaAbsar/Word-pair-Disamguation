# Testitng
# Disambiguate the pseudowords
# Phase 4
import pandas as pd

def disambiguate(test_data, priors, pseudoword, output_dir):
    predicted = {}
    for line in test_data:
        words = line.split()
        # Save the P(c) values in a dictionary where keys are the class names
        prob_class = {}
        for c in priors.keys():
            # extract the prior prob of class c in prob_c
            prob_c = priors[c]
            prob_w_given_c = dict(pd.read_csv(output_dir+f"_{c}"+"_Wprob.txt", delimiter=": ", \
                header=None, engine='python').to_dict(orient='split')['data'])
            for w in words:
                if not w == 'null': prob_c *= prob_w_given_c[w] #compute: P(c) = Prior(c)*product(P(w|c))
            prob_class[c] = prob_c
        predicted[line] = max(prob_class, key=prob_class.get)   # predicted class is the one with max prob.
    # save the predicted result into a file
    path = output_dir+f"_{pseudoword}"+"_predicted.txt"
    with open(path, 'w') as f:
        for line in predicted:
            if not line == '': f.write("%s: %s\n" %(str(line), predicted[line]))
    return(predicted)