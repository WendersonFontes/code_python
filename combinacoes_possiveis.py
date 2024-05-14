import itertools

def generate_sequences(limit=10):
    numbers = list(range(1, 20))
    sequences = []
    count = 0  # Inicializa um contador

    for combo in itertools.combinations(numbers, 5):
        if count >= limit:
            break  # Sai do loop quando o limite é atingido
        sequence = list(combo)
        sequences.append(sequence)
        count += 1  # Incrementa o contador

    return sequences

result = generate_sequences()
print(result)
