from collections import Counter

c = Counter()

for ch in 'Programming':
    c[ch] = c[ch] + 1

print c