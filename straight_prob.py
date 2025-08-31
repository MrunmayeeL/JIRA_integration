import random

def simulate_large_straight():
    """Simulates a single roll of five dice and checks for a large straight."""
    dice = sorted([random.randint(1, 6) for _ in range(5)])
    if dice == [1, 2, 3, 4, 5] or dice == [2, 3, 4, 5, 6]:
        return True
    return False

def estimate_large_straight_probability(trials):
    """Runs a Monte Carlo simulation to estimate large straight probability."""
    successes = sum(1 for _ in range(trials) if simulate_large_straight())
    return successes / trials

if __name__ == "__main__":
    num_trials = 100000
    probability = estimate_large_straight_probability(num_trials)
    print(f"Estimated probability of rolling a large straight: {probability:.6f}")