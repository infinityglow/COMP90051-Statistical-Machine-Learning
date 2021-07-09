import pandas as pd
import numpy as np

def get_pairs(data):
    pairs = set()
    for entry in data:
        entry = entry.strip('\n').split()
        for i in range(len(entry)-1):
            for j in range(i+1, len(entry)):
                pairs.add((int(entry[i]), int(entry[j])))
    return pairs

def check_duplicates(pairs, test):
    cnt = 0
    for source, link in test:
        if (source, link) in pairs:
            print("Duplicate")
            print((source, link))
            cnt += 1
    print(cnt)

def preprocess(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    pairs = get_pairs(data)
    return pairs

with open("../data/train.txt", 'r') as f:
    train_set = f.readlines()

test_set = pd.read_csv("../data/test-public.csv")
test_set = test_set[['Source', 'Sink']].values

# pairs = preprocess("../data/train.txt")
# f = open("../pairs.txt", 'w')
# for pair in pairs:
#     f.writelines("%d %d\n" % (pair[0], pair[1]))
# check_duplicates(pairs, test_set)


