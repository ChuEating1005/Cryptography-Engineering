def calculate_letter_frequencies(ciphertext):
    frequencies = {}
    for char in ciphertext:
        if char.isalpha():
            if char in frequencies:
                frequencies[char] += 1
            else:
                frequencies[char] = 1
    return frequencies

ciphertext = """
C UYGHARMZ IUWMPRWIR GAIR YVRMP
MBHMZWMPUM C VMMXWPE YV PYR VCZ
ZMGYQMD VZYG CXCZG YP CPCXKTWPE CPD MBHXYZM
RNM VXYYD YV CDQCPUMD OPYSXMDEM SNWUN MCUN
KMCZ LZWPEI SWRN WR
"""

frequencies = calculate_letter_frequencies(ciphertext)
for letter, freq in sorted(frequencies.items()):
    print(f"{letter}: {freq}")
