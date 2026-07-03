#!/usr/bin/env python3

import argparse
import csv
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('train_file')
ap.add_argument('test_file')
args = ap.parse_args()


def read_data(filename):
    id_, age, feats, title, text = [], [], [], [], []
    with open(filename, 'rt', encoding='utf8') as f:
        csvr = csv.reader(f, delimiter='\t')
        # skip the header
        _ = next(csvr)
        for row in csvr:
            id_.append(int(row[0]))
            age.append(int(row[1]))
            feats.append([float(x) for x in row[2:52]])
            title.append(row[52])
            text.append(row[53])

    return id_, np.array(age), np.array(feats), title, text


_, trn_age, trn_feats, trn_title, trn_text = read_data(args.train_file)
tst_id, _, tst_feats, tst_title, tst_text = read_data(args.test_file)

minage, maxage = trn_age.min(), trn_age.max()
pred = np.random.randint(minage, maxage, trn_age.shape)
r2 = 1 - np.square(trn_age - pred).sum() \
        / np.square(trn_age - trn_age.mean()).sum()
print(f"R-squared on training set: {r2}")

method = 'baseline'
with open(f'a1-{method}.predictions', 'wt') as f:
    print("id\tage", file=f)
    for id_, pred in zip(tst_id, pred):
        print(f"{id_}\t{pred}", file=f)
