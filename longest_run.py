import random

def find_longest_run(flips):
    """Finds the longest consecutive run of identical flips."""
    max_run = 0
    current_run = 0
    if not flips:
        return 0

    for i in range(len(flips)):
        if i > 0 and flips[i] == flips[i-1]:
            current_run += 1
        else:
            current_run = 1
        max_run = max(max_run, current_run)
    return max_run

def estimate_longest_run_average(simulations):
    """Runs a Monte Carlo simulation to estimate the average longest run."""
    total_longest_run = 0
    num_flips = 200
    
    for _ in range(simulations):
        flips = [random.choice(['H', 'T']) for _ in range(num_flips)]
        total_longest_run += find_longest_run(flips)
        
    return total_longest_run / simulations

if __name__ == "__main__":
    num_simulations = 10000
    average_longest_run = estimate_longest_run_average(num_simulations)
    print(f"Estimated average longest run in 200 flips: {average_longest_run:.2f}")