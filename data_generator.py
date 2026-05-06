import random
import csv

def generate_sequence():
    sequence = []

    for _ in range(5):
        step = [
            random.randint(10, 120),
            round(random.uniform(1, 10), 2),  # cleaner float
            random.randint(0, 50),
            random.randint(0, 20),
            random.randint(1, 10)
        ]
        sequence.extend(step)

    avg_actions = sum(sequence[1::5]) / 5
    avg_items = sum(sequence[2::5]) / 5

    if avg_actions > 7:
        label = 1
    elif avg_items > 30:
        label = 2
    else:
        label = 0

    if label not in [0, 1, 2]:
        return None

    return sequence + [label]

with open("players_seq.csv", "w", newline="") as f:
    writer = csv.writer(f)

    headers = [f"f{i}" for i in range(25)] + ["label"]
    writer.writerow(headers)

    count = 0
    while count < 1000:
        row = generate_sequence()
        if row and len(row) == 26:
            writer.writerow(row)
            count += 1