import matplotlib.pyplot as plt
import numpy as np

input = open("output_tweets_3/part-00000", "r")
words = []
counts = []
for line in input:
    line = line.strip()
    line_vals = line.split("\t")
    words.append(line_vals[0])
    counts.append(int(line_vals[1]))

inx_sorted = np.argsort(counts)
counts = [counts[i] for i in inx_sorted]
words = [words[i] for i in inx_sorted]

x = range(len(words))
plt.bar(x, counts)
plt.xlabel("Pronouns")
plt.ylabel("Counts")
plt.xticks(x, words)
plt.show()
