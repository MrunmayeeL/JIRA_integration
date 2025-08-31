import random

def simulate_yahtzee():
    """Simulates a single roll of five dice and checks for a Yahtzee."""
    dice = [random.randint(1, 6) for _ in range(5)]
    return len(set(dice)) == 1

def estimate_yahtzee_probability(trials):
    """Runs a Monte Carlo simulation to estimate Yahtzee probability."""
    successes = sum(1 for _ in range(trials) if simulate_yahtzee())
    return successes / trials

if __name__ == "__main__":
    num_trials = 100000  # Number of simulation trials
    probability = estimate_yahtzee_probability(num_trials)
    print(f"Estimated probability of rolling a Yahtzee: {probability:.6f}")