datas = [[4, 8], [10, 26], [27, 7]]

ans_a = 0
ans_b = 0
for a in range(30):
    for b in range(30):
        check = 1
        for pair in datas:
            if (pair[1] % 30 != (a * pair[0] + b )% 30):
                check = 0
                break
        if(check == 1):
            ans_a = a
            ans_b = b
print(str(ans_a) + " " + str(ans_b))