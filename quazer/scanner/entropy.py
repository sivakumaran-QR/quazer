import math

def shannon_entropy(data):
    prob = [float(data.count(c)) / len(data) for c in dict.fromkeys(list(data))]
    return -sum([p * math.log(p) / math.log(2.0) for p in prob])

def is_high_entropy(string):
    return shannon_entropy(string) > 4.5