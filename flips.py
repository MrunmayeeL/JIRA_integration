import random

def simulate_five_heads_in_a_row():
    """Simulates coin flips until five heads in a row are achieved."""
    flips_count = 0
    consecutive_heads = 0
    
    while consecutive_heads < 5:
        flip = random.choice(['H', 'T'])
        flips_count += 1
        
        if flip == 'H':
            consecutive_heads += 1
        else:
            consecutive_heads = 0
            
    return flips_count

def estimate_flips_for_five_heads(simulations):
    """Runs a Monte Carlo simulation to estimate the average flips."""
    total_flips = sum(simulate_five_heads_in_a_row() for _ in range(simulations))
    return total_flips / simulations

if __name__ == "__main__":
    num_simulations = 10000
    average_flips = estimate_flips_for_five_heads(num_simulations)
    print(f"Estimated average flips for 5 heads in a row: {average_flips:.2f}")