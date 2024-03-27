def lfsr(seed, taps, length):
    """Generate a keystream using LFSR given a seed, tap positions, and desired length."""
    sr, xor = seed, 0
    keystream = []
    for _ in range(length):
        for t in taps:
            xor ^= int(sr[t-1])     # XOR tap positions
        keystream.append(sr[-1])    # Append the output bit
        sr = str(xor) + sr[:-1]     # Shift register
        xor = 0                     # Reset xor
    return ''.join(keystream)

def text_to_bits(text):
    """Convert text to its binary representation."""
    return ''.join(format(ord(i), '08b') for i in text)

def bits_to_text(bits):
    """Convert binary representation back to text."""
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def xor_strings(s1, s2):
    """XOR two binary strings."""
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(s1, s2))

# Given parameters
plaintext = """
ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRAN
SCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCO
MPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUET
OBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMU
CHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLT
HATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSI
TYINTHEFIRSTPLACE
"""
initial_key = "00000001"
# Convert plaintext to binary
plaintext_binary = text_to_bits(plaintext)

# Define the characteristic polynomial's tap positions (note: positions are from the end of the register)
tap_positions = [8, 4, 3, 2]  # Corresponding to x^8 + x^4 + x^3 + x^2 + 1

# Generate keystream
keystream = lfsr(initial_key, tap_positions, len(plaintext_binary))

# Encrypt the plaintext
ciphertext_binary = xor_strings(plaintext_binary, keystream)

# Decrypt the ciphertext (the operation is identical due to the symmetry of XOR)
decrypted_binary = xor_strings(ciphertext_binary, keystream)

# Convert binary back to text
decrypted_text = bits_to_text(decrypted_binary)

# Check if decryption is correct
if decrypted_text == plaintext:
    print("Decryption successful, plaintext is:", decrypted_text)
else:
    print("Decryption failed.")

