import matplotlib.pyplot as plt

input = open("output_letter_8/part-00000", "r")
letters = []
counts = []
for line in input:
    line = line.strip()
    line_vals = line.split("\t")
    letters.append(line_vals[0])
    counts.append(line_vals[1])

# Remove the last letter (ae) since python had a hard time plotting it
letters.pop(-1)
counts.pop(-1)

x = range(len(letters))
plt.bar(x, counts)
plt.xlabel("Letters")
plt.ylabel("Counts")
plt.xticks(x, letters)
plt.show()
