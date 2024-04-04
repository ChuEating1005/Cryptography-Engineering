import os
import random

def get_high_entropy_seed(size=32):
    """Reads a specified number of bytes from /dev/urandom."""
    return os.urandom(size)

for _ in range(10):
    seed_bytes = get_high_entropy_seed()
    int_value = int.from_bytes(seed_bytes, byteorder='big')
    random.seed(int_value)
    print(random.random())