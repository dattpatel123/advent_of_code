import random

# Configure size of test
NUM_RANGES = 200_000
NUM_IDS = 300_000
MAX_VALUE = 10_000_000

output_file = "large_test_input.txt"

with open(output_file, "w") as f:
    # Generate ranges
    for _ in range(NUM_RANGES):
        a = random.randint(0, MAX_VALUE)
        b = a + random.randint(0, 5000)  # ranges of limited width
        f.write(f"{a}-{b}\n")

    # Blank line to separate ranges from ids
    f.write("\n")

    # Generate ids
    for _ in range(NUM_IDS):
        f.write(f"{random.randint(0, MAX_VALUE)}\n")

print(f"Generated test file: {output_file}")
