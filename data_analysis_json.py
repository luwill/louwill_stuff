#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@author: louwill
@contact: ygnjd2016@gmail.com
@file: json_exercise1.py
@time: 2018/4/17 22:42
'''

import pandas as pd
import numpy as np
import json
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

records = [json.loads(line) for line in open('./example1.txt')]
tz = [rec['tz'] for rec in records if 'tz' in rec]
frame = pd.DataFrame(records)
cframe = frame[frame.a.notnull()]
cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', 'os'])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
print(agg_counts.take(indexer[-10:]))


def count_tz(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    counts.pop('')
    return counts

def top_counts(dict_counts, n=10):
    key_value_pairs = [(counts, tz) for (tz, counts) in dict_counts.items()]
    key_value_pairs.sort()
    return key_value_pairs[-n:]


def main():
    tz_counts = count_tz(tz)
    tz_top10_frame = pd.DataFrame(top_counts(tz_counts))
    tz_top10_frame = tz_top10_frame.sort_values(by=0, ascending=False)
    sns.barplot(y=tz_top10_frame[1], x=tz_top10_frame[0])
    plt.show()


if __name__ == '__main__':
    main()
