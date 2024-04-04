import hashlib
import time

def calculate_checksum(file_path, hash_function):
    hash_func = getattr(hashlib, hash_function)()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def measure_time(file_path, hash_function):
    start_time = time.time()
    calculate_checksum(file_path, hash_function)
    end_time = time.time()
    return end_time - start_time

file_path = 'video.mp4'
hash_functions = ['md5', 'sha1', 'sha224', 'sha256', 'sha512', 'sha3_224', 'sha3_256', 'sha3_512']

results = {}

for hash_function in hash_functions:
    elapsed_time = measure_time(file_path, hash_function)
    results[hash_function] = elapsed_time
    print(f"{hash_function}: {elapsed_time:.4f} s")

# Answering (b) and (c)
fastest = min(results, key=results.get)
sorted_functions = sorted(results, key=results.get)

print(f"\nFastest hash function: {fastest}")
print("Hash functions ranked by speed:")
for rank, function in enumerate(sorted_functions, start=1):
    print(f"{rank}. {function} ({results[function]:.4f} s)")
