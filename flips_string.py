import random

def simulate_string_occurrence(target_string):
    """Simulates flips until a target string is found."""
    flips_count = 0
    current_string = ""
    target_length = len(target_string)
    
    while True:
        flip = random.choice(['H', 'T'])
        current_string += flip
        flips_count += 1
        
        # Check if the target string is at the end of the current string
        if len(current_string) >= target_length and current_string.endswith(target_string):
            return flips_count

def estimate_flips_for_string(target_string, simulations):
    """Runs a Monte Carlo simulation to estimate the average flips."""
    total_flips = sum(simulate_string_occurrence(target_string) for _ in range(simulations))
    return total_flips / simulations

if __name__ == "__main__":
    target_string = "HHTTH"
    num_simulations = 10000
    average_flips = estimate_flips_for_string(target_string, num_simulations)
    print(f"Estimated average flips for string '{target_string}': {average_flips:.2f}")