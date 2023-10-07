# Create Pseudowords following phase 0
# Phase 2

def pseudo_replace(output_dir,sense_list, pseudoword):
    # Form a dictionary with key as the sense word
    # and context with pseudoword replaces as the value
    # seperately for train and test
    train_dict = {}
    ground_truth = {}
    test_data = []
    sense_prior = {}    # Compute priors
    for sense in sense_list:
        train_path = output_dir+f"_{sense}"+"_train.txt"
        test_path = output_dir+f"_{sense}"+"_test.txt"
        sense_prior[sense] = 0
        with open(train_path, 'r') as file:
            c = file.read().split('\n')
            train_dict[sense] = []  # Create a labeled dataset for training
            for line in c:
                if not line == '':
                    sense_prior[sense] += 1                              
                    # Replace the sense word with the pseudoword from the pseudoword_dict
                    train_dict[sense].append(line.replace(f"{sense}", pseudoword, 1))
        with open(test_path, 'r') as file:
            c = file.read().split('\n')
            ground_truth[sense] = []
            for line in c:
                if not line == '':
                    ground_truth[sense].append(line.replace(f"{sense}", pseudoword, 1))
                    test_data.append(line.replace(f"{sense}", pseudoword, 1))
    # Save the ground truth file for accuracy check
    path = output_dir+f"_{pseudoword}"+"_groundtruth.txt"
    with open(path, 'w') as f:
        for sense in ground_truth:
            for line in ground_truth[sense]:
                if not line == '': f.write("%s: %s\n" %(line, str(sense)))
    return(train_dict, test_data, sense_prior)