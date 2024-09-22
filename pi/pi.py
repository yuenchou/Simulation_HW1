import random

# Function to estimate the value of pi using Monte Carlo methods
def estimate_pi(num_samples):
    num_inside = 0
    for i in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            num_inside += 1
    pi_estimate = 4 * num_inside / num_samples
    return pi_estimate

for i in range(2, 2048, 2):
    pi_estimate = estimate_pi(i)
    print("Estimated value of pi:", pi_estimate)