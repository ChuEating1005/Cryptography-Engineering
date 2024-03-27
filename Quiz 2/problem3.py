input_str = '''
UONCS VAIHG EPAAH IGIRL BIECS
TECSW PNITE TIENO IEEFD OWECX
TRSRX STTAR TLODY FSOVN EOECO
HENIO DAARQ NAELA FSGNO PTE
'''
rows = 14
cols = 7
table = [[None for _ in range(cols)] for _ in range(rows)]

cnt = 0
for c in input_str:
    if(not c.isalpha()): continue
    table[cnt % rows][int(cnt / rows)] = c
    cnt += 1

vowel = ['A', 'E', 'I', 'O', 'U']
diff_sum = 0
diff_list = [None] * rows

column_permutation = [4, 1, 5, 6, 0, 3, 2]
print("Ciphertext:")
for i in range(rows):
    cnt_vowel = 0
    for j in range(cols):
        print(f"{table[i][j]} ", end='')
        if(table[i][j] in vowel): cnt_vowel += 1
    diff_list[i] = abs(cnt_vowel - 0.4 * cols)
    print('')
print('')
for i in range(rows):
    print(f"{i + 1} line difference: {diff_list[i]:1.2f}")
    diff_sum += diff_list[i]
diff_sum /= rows
print(f'\nDifference Avg: {diff_sum:1.2f}')



