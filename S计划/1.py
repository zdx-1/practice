cnt = 0
for i in range(1, 20240602):
    for j in range(1, 20240602):
        if (i ** i + j ** j) % 6421 == 0:
            cnt += 1
            print(i, j, cnt)
