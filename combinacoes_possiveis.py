import itertools

def generate_sequences():
    numbers = list(range(1, 20))
    sequences = []

    for combo in itertools.combinations(numbers, 5):
        sequence = list(combo)
        sequences.append(sequence)

    return sequences

result = generate_sequences()
print(result)
