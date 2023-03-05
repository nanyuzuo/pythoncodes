
mark = [56,78,73,92,87,98,28,91,85,70,66,45,93]
i = 0
while i < 12:
    j = i + 1
    while j < 13:
        A = mark[i] 
        B = mark[j] 
        if A > B:
            mark[i] = B
            mark[j] = A
        j = j + 1
    i = i + 1
print(f"本班最高分为{mark[12]}本班最低分为{mark[0]}")


