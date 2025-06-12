import random

def generate_signal():
    directions = ["Buy", "Sell"]
    pairs = ["EUR/USD", "USD/JPY", "GBP/USD"]
    times = ["1 min", "5 min"]

    if random.random() > 0.5:
        return f"{random.choice(pairs)} - {random.choice(directions)} ({random.choice(times)})"
    return None
